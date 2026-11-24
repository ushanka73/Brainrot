### 5. Modul `main.py` — **Altha**
Fokus ke mesin utama dan penggabungan semua modul:
* Membangun *game loop* dengan **Pygame** dan *state machine* untuk mengatur perpindahan layar aktif.
* Menjalankan **alur giliran 8 langkah**: baca tombol arah, abaikan jika menabrak dinding, gerakkan Dava, cek pintu EXIT (lanjut lantai atau menang), jalankan `search.py` untuk Hytam & Bayang (khusus lantai 3), serta cek kondisi tertangkap termasuk kasus bertukar tempat.
