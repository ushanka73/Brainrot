# Brainrot
### 1. Modul `maze.py` — **Dava**
Fokus ke data peta dan struktur labirin:
* Menyimpan data 3 rancangan labirin berukuran 13×15 (*Otak Kiri*, *Otak Tengah*, *Otak Kanan*) pakai simbol `#`, `.`, `D`, `H`, `B`, dan `E`.
* Bikin fungsi pembaca grid untuk mengekstrak koordinat awal `(baris, kolom)` Dava, Hytam, Bayang, dan pintu EXIT.
* Bikin fungsi pengacakan urutan ketiga lantai setiap kali permainan baru dimulai.

### 2. Modul `search.py` — **Hayden**
Fokus ke otak kecerdasan buatannya:
* Bikin fungsi `heuristic(n, t)` dengan rumus jarak Manhattan $\vert{}b(n)-b(t)\vert{} + \vert{}k(n)-k(t)\vert{}$.
* Bikin fungsi pencari tetangga 4 arah (atas, bawah, kiri, kanan) yang bukan dinding.
* Implementasi `best_first_search(grid, start, goal)` memakai modul `heapq` yang mengembalikan daftar jalur.
* Bikin fungsi target **Bayang**: menelusuri maksimal 3 sel ke depan sesuai arah gerak terakhir Dava, dan berhenti di sel terakhir sebelum dinding.

### 3. Modul `verify.py` & `storage.py` — **Benny**
Fokus ke pengujian algoritma dan penyimpanan data:
* **`verify.py`:** Skrip penelusuran ruang keadaan (*state-space*) pakai *Breadth-First Search* untuk memverifikasi bahwa 3 labirin buatan Dava pasti bisa dimenangkan (baik lawan Hytam saja maupun Hytam + Bayang), sekaligus mencatat jumlah langkah minimumnya.
* **`storage.py`:** Fungsi baca/tulis rekor *Top Floor* ke file JSON (hanya menimpa data jika lantai yang dicapai lebih tinggi dari rekor sebelumnya).

### 4. Modul `render.py` & `ui.py` — **Arya**
Fokus penuh ke tampilan visual dan antarmuka:
* **`render.py`:** Menggambar grid labirin, karakter Dava (stickman), Hytam, Bayang, pintu EXIT, dan penanda titik bidik Bayang menggunakan **Pycairo**.
* **`ui.py`:** Membuat tampilan dan tombol untuk Menu Utama (*Mulai Game*, *Top Floor*, *Keluar*), Menu Jeda (*Menu*, *Quit*), layar Menang, layar Kalah, dan layar Top Floor.

### 5. Modul `main.py` — **Altha**
Fokus ke mesin utama dan penggabungan semua modul:
* Membangun *game loop* dengan **Pygame** dan *state machine* untuk mengatur perpindahan layar aktif.
* Menjalankan **alur giliran 8 langkah**: baca tombol arah, abaikan jika menabrak dinding, gerakkan Dava, cek pintu EXIT (lanjut lantai atau menang), jalankan `search.py` untuk Hytam & Bayang (khusus lantai 3), serta cek kondisi tertangkap termasuk kasus bertukar tempat.
