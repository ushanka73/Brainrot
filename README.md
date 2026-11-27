## Pembagian Tugas

| Anggota | Modul dan Aset | Tugas |
| :--- | :--- | :--- |
| **Hayden** | Asset (Tembok, Pintu, Player, Enemy 1/2), `display/pygame_bridge.py` | Bikin tekstur; mengubah hasil gambar Pycairo agar bisa ditampilkan di jendela Pygame. |
| **Arya** | `display/render.py`, PNG (Lantai 1, Lantai 2, Enemy 1) | Membuat aset tersebut dengan Pycairo dan menyimpannya sebagai PNG. Di `render.py`, memuat PNG, memetakan layout maze ke posisi layar, lalu menggambar maze dan objek. |
| **Linggoy** | `core/search.py`, `maze.py`, `verify.py` | Membuat Best First Search yang dipakai kedua pengejar dengan target sesuai perilaku masing-masing. Membuat layout maze dan posisi awal objek, serta memeriksa validitas dan keterhubungan maze. |
| **Dava** | `main.py`, `core/turn.py`, `config.py` | Mengatur game loop dan integrasi modul; mengatur gerakan serta giliran pemain dan pengejar, tabrakan, dan menang/kalah; menyimpan pengaturan game dan data progres lantai. |
| **Benny** | `storage.py`, `display/ui.py` | Menyimpan dan membaca rekor Top Floor. Mengatur alur layar menu utama, jeda, menang, gagal, dan Top Floor, termasuk aksi tombolnya. |
```[cite: 2]
