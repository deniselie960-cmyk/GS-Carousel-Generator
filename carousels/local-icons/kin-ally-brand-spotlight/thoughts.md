# Thoughts — Kin + Ally Brand Spotlight

## Tujuan

Membuat carousel Brand Spotlight Kin + Ally untuk Local Icons dalam format Instagram `4:5`. Carousel harus terasa konsisten dengan template Local Icons yang sudah ada, tetapi tetap memberi ruang bagi karakter Kin + Ally sebagai brand activewear dan perlengkapan yoga yang modern.

Output akhir terdiri dari lima slide dengan ukuran kerja `1080 × 1350px` dan hasil render `2160 × 2700px`.

## Arahan utama

- Mengikuti sistem visual di `carousels/local-icons/design.md`.
- Memakai header resmi Local Icons pada setiap slide.
- Menggunakan Gotham, bidang putih atau cream, bentuk lingkaran berwarna yang terpotong di tepi, serta kartu foto dengan sudut membulat dan bayangan lembut.
- Menjaga visual tetap ringan, bersih, dan mudah dibaca di layar ponsel.
- Menggunakan warna Kin + Ally Fiord pada logo dan beberapa elemen teks, tanpa mengubah sistem warna utama Local Icons.
- Tidak memakai simbol club Kin + Ally sebagai elemen dekoratif berulang.
- Tidak mengubah copywriting yang diberikan.

## Ketentuan copy

Copy dipertahankan sesuai brief, termasuk:

- `Literally lebih dari sekedar produk — ini journey mereka.`
- `Geser`
- Seluruh paragraf pada Slide 2.
- `Buy 2 disc 6%`
- `Buy 3 disc 8%`
- `Buy 4 disc 10%`
- `Mix All items`

Kata `sekedar` tidak dikoreksi menjadi `sekadar` karena arahan pengguna meminta copy tetap sama.

## Pemikiran per slide

### Slide 1 — Cover

Cover mengikuti struktur Brand Spotlight Local Icons: identitas Local Icons di bagian atas, label `BRAND SPOTLIGHT`, logo brand, pernyataan utama, foto vertikal, dan petunjuk `Geser`.

Foto yang digunakan adalah `kin-ally-mats-duo.jpeg`. Foto ini sebelumnya berada di Slide 5, kemudian dipindahkan ke cover agar produk mat langsung terlihat pada impresi pertama. Ukuran kartu foto dikurangi secara bertahap berdasarkan feedback pengguna: pertama `10px`, kemudian dikurangi lagi `30px`. Ukuran akhirnya adalah `408 × 830px` pada canvas kerja.

### Slide 2 — Brand story

Paragraf yang panjang membutuhkan layout editorial dua kolom. Foto yoga ditempatkan di kiri, sementara seluruh copy berada di dalam kartu putih di kanan. Ukuran body copy dijaga pada `25px`, masih berada di atas batas minimum yang ditetapkan oleh design guide.

Foto `kin-ally-yoga-strap.jpeg` dipilih karena menunjukkan activewear, mat, cork blocks, dan strap dalam satu komposisi. Accent rule kuning–teal membantu menghubungkan kartu editorial ini dengan bahasa visual Local Icons.

### Slide 3 — Product showcase

Slide ini sengaja tidak memakai title atau headline. Satu-satunya identitas grafis adalah header resmi Local Icons; isi utama hanya berupa foto produk.

Komposisi memakai:

- `kin-ally-yoga-wheels.jpeg` sebagai foto utama.
- `kin-ally-mats-duo.jpeg` untuk memperlihatkan variasi mat.
- `kin-ally-yoga-duo.jpeg` sebagai detail mat dan cork blocks.

Crop diarahkan ke mat, yoga wheels, dan blocks agar produk tetap menjadi fokus meskipun sumber fotonya bersifat lifestyle.

### Slide 4 — Product showcase

Slide ini juga tidak memakai title atau headline. Susunan foto dibuat berbeda dari Slide 3 agar ritme carousel tidak terasa berulang.

Komposisi memakai:

- `kin-ally-gear.jpeg` sebagai hero image karena mat dan cork blocks terlihat jelas.
- `kin-ally-yoga-duo.jpeg` untuk detail mat dan blocks saat digunakan.
- `kin-ally-yoga-strap.jpeg` untuk menampilkan mat, blocks, dan straps.

Slide 3 memakai cream dengan aksen kuning–teal, sedangkan Slide 4 memakai putih dengan aksen biru–ungu.

### Slide 5 — Offer

Offer disusun sebagai tiga kartu bertingkat supaya hubungan antara jumlah pembelian dan diskon dapat dipahami dengan cepat. Warna kartu bergerak dari putih ke kuning lalu ungu untuk membangun hierarki.

Foto yang digunakan adalah `kin-ally-yoga-duo.jpeg`, yaitu foto yang sebelumnya berada di cover. Pertukaran foto dilakukan sesuai feedback pengguna. Crop mempertahankan pose atletik sekaligus memperlihatkan mat dan cork blocks.

## Penggunaan aset

- Logo Kin + Ally: `assets/kin-ally-logo.png`
- Local Icons lockup sumber: `assets/local-icons-lockup-horizontal.svg`
- Local Icons lockup render-stable: `assets/local-icons-lockup-horizontal.png`
- Swipe icon: `assets/right.png`
- Foto cover: `assets/kin-ally-mats-duo.jpeg`
- Foto story: `assets/kin-ally-yoga-strap.jpeg`
- Foto produk: seluruh foto Kin + Ally di folder `assets/`
- Foto offer: `assets/kin-ally-yoga-duo.jpeg`

Versi PNG dari lockup Local Icons dibuat dari SVG resmi karena referensi SVG sempat tidak tampil secara konsisten pada beberapa render. Raster tersebut mempertahankan artwork yang sama dan membuat hasil ekspor lebih deterministik.

## Hal yang sengaja tidak dilakukan

- Tidak menambahkan slide penutup keenam.
- Tidak menambahkan headline pada Slide 3 dan Slide 4.
- Tidak menulis ulang atau memperbaiki copy.
- Tidak memakai club symbol sebagai pattern atau ornamen.
- Tidak menambahkan klaim, caption produk, harga, QR code, tanggal, atau CTA yang tidak ada di brief.
- Tidak mengedit atau mengubah warna produk di dalam foto.

## QA

- Semua slide dirender pada `2160 × 2700px`.
- Semua aset lokal dan referensi file telah diperiksa.
- Slide 3 dan Slide 4 tidak memiliki elemen teks terlihat selain lockup resmi Local Icons.
- Cover dan Slide 5 diperiksa kembali setelah pertukaran foto.
- Ukuran cover photo terakhir sudah mencerminkan seluruh revisi pengguna.
- Copy di HTML dan `content/story.json` tetap mengikuti brief.

