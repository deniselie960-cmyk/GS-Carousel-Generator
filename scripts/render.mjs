import { existsSync, mkdirSync, readdirSync } from "node:fs";
import { createRequire } from "node:module";
import { dirname, join, resolve } from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";

const require = createRequire(import.meta.url);
const { chromium } = require("playwright");

const root = resolve(dirname(fileURLToPath(import.meta.url)), "..");
const slidesDir = join(root, "slides");
const outputDir = join(root, "rendered");
const args = new Set(process.argv.slice(2));
const type = args.has("--jpg") ? "jpeg" : "png";
const extension = type === "jpeg" ? ".jpg" : ".png";
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
  for (const slide of slides) {
    const context = await browser.newContext({
      viewport: { width: 1080, height: 1350 },
      deviceScaleFactor: 2,
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
