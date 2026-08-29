import { existsSync, mkdirSync, readdirSync } from "node:fs";
import { createRequire } from "node:module";
import { dirname, join, resolve, sep } from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";

const require = createRequire(import.meta.url);
const { chromium } = require("playwright");

const root = resolve(dirname(fileURLToPath(import.meta.url)), "..");
const rawArgs = process.argv.slice(2);
const args = new Set(rawArgs);
const type = args.has("--jpg") ? "jpeg" : "png";
const extension = type === "jpeg" ? ".jpg" : ".png";
const scaleArgument = rawArgs.find((argument) => argument.startsWith("--scale="));
const scale = scaleArgument ? Number(scaleArgument.split("=", 2)[1]) : 2;

if (!Number.isFinite(scale) || scale <= 0) {
  throw new Error("Render scale must be a positive number, for example --scale=1.");
}
const campaignArgument = rawArgs.find((argument) => !argument.startsWith("--"))
  ?? "carousels/niceso/brand-origin";
const campaignDir = resolve(root, campaignArgument);
const carouselsRoot = resolve(root, "carousels") + sep;

if (!campaignDir.startsWith(carouselsRoot)) {
  throw new Error("Campaign path must be inside the carousels directory.");
}

const slidesDir = join(campaignDir, "slides");
const outputDir = join(campaignDir, "rendered");

if (!existsSync(slidesDir)) {
  throw new Error(`Slides directory not found: ${slidesDir}`);
}
const browserCandidates = [
  process.env.CAROUSEL_BROWSER,
  "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
  "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe",
].filter(Boolean);
const executablePath = browserCandidates.find((path) => existsSync(path));

if (!existsSync(outputDir)) mkdirSync(outputDir, { recursive: true });

const slides = readdirSync(slidesDir)
  .filter((name) => /^slide-\d+\.html$/i.test(name))
  .sort();

const browser = await chromium.launch({
  headless: true,
  ...(executablePath ? { executablePath } : {}),
});

try {
  console.log(`Campaign: ${campaignArgument}`);
  for (const slide of slides) {
    const context = await browser.newContext({
      viewport: { width: 1080, height: 1350 },
      deviceScaleFactor: scale,
    });
    const page = await context.newPage();
    const url = pathToFileURL(join(slidesDir, slide)).href;
    await page.goto(url, { waitUntil: "load" });
    await page.evaluate(() => document.fonts.ready);
    const outputPath = join(outputDir, slide.replace(/\.html$/i, extension));
    await page.screenshot({
      path: outputPath,
      type,
      ...(type === "jpeg" ? { quality: 94 } : {}),
      fullPage: false,
    });
    console.log(`Rendered ${slide} -> ${outputPath}`);
    await context.close();
  }
} finally {
  await browser.close();
}
