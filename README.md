# Proyek Kolaborasi Python ALT-F4

Selamat datang di Proyek Kolaborasi Python ALT-F4. Repositori ini merupakan hasil kerjasama kami dalam melakukan tugas kuliah 

## Anggota Kolaborasi

- **Rainer Jason Hamdani** ([Raiijh](https://github.com/Raiijh))
- **Timothy Kylen Sulangi** ([mottkaiii](https://github.com/mottkaiii))
- **Dennise Theo Sumenda** ([dennisesumenda-glitch](https://github.com/dennisesumenda-glitch))


## Deskripsi Proyek

Proyek ini adalah implementasi digital fungsional dari permainan klasik Tic-Tac-Toe (atau Noughts and Crosses). Program ini dibuat menggunakan bahasa Python dan menggunakan antarmuka pengguna grafis (GUI) standar Tkinter.

Program ini bertujuan untuk memberikan pengalaman bermain dua pemain yang lancar di mana pemain dapat mendaftarkan nama mereka sebelum permainan dimulai. Dua modul utama program adalah gui_app.py, yang berfungsi sebagai frontend dan menangani event klik, visualisasi, dan pembaruan tampilan. Tictactoe_logic.py berfungsi sebagai backend dan mengelola status papan, aturan kemenangan, dan skor. Pelacakan skor multi-ronde, tampilan garis kemenangan yang jelas, dan tombol reset yang efisien adalah fitur utamanya, yang menjamin pembagian masalah yang baik dalam arsitektur kode.

## Fitur-fitur
 |             Kategori            |           Fitur            | Detail kode | 
|-----------------|-------|-------------|
| Logika Inti  | Struktur Papan dan Status                 |Representasi 1D: Papan diwakili sebagai list 1 dimensi berukuran 9. Properti: self.papan = [""] * 9 Logika menggunakan indeks 0 hingga 9 untuk melacak posisi pemain. input).           
|              | Logika Kemenangan              | Kombinasi Kunci: Daftar tuple berisi indeks kemenangan (misalnya, (0, 1, 2) untuk baris atas). Properti: self.menang_kombinasi = [(0, 1, 2), (3, 4, 5), ..., (0, 4, 8)] Metode: cek_menang() mengulang (loop) daftar ini.             
|          | Aturan Validasi Gerakan                  | Pengecekan: Dijalankan di awal lakukan_gerakan(i). Fragmen Kode: if self.game_aktif and self.papan[i] == "": Ini memastikan gerakan hanya terjadi jika permainan aktif dan kotak kosong (mirip dengan mengecek kotak non-bom yang belum terbuka).                
|           | Penggantian Giliran                  | Logika Sederhana: Tidak ada timer atau rule kompleks. Fragmen Kode: self.pemain_saat_ini = 'O' if pemain == 'X' else 'X' (dilakukan setelah gerakan valid dan belum ada pemenang).   

## Panduan Instalasi
- [Python](https://www.python.org/downloads/release/python-3140/)
- [Git](https://github.com/git-for-windows/git/releases/download/v2.52.0.windows.1/Git-2.52.0-64-bit.exe)
 > Jika belum terinstall, tekan "Python" atau "Git" di atas.

 ### *Cloning repository*
1. Salin link repositori ini: https://github.com/Raiijh/Proyek-Kolaborasi-Python---ALT-F4-.git
2. Buka terminal dan pilih folder yang akan dijadikan tempat kloning repositori
```bash
  cd "[direktori folder yang ingin anda digunakan]"
```
3. Salin repositori program ke dalam folder menggunakan fungsi '**git clone**'
```bash
  git clone https://github.com/Raiijh/Proyek-Kolaborasi-Python---ALT-F4-.git
```


## Cara Menajalankan Program

1. Clone repository:
   ```bash
   git clone https://github.com/Raiijh/Proyek-Kolaborasi-Python---ALT-F4-.git
   ```
2. Masuk ke direktori:
   ```bash
   cd Proyek-Kolaborasi-Python---ALT-F4-
   ```
3. jalankan permainan
   ```bash
   python gui_app.py
   ```

## Dokumentasi Teknis (Flowchart)
 ### *Flowchart Logika*
<img width="789" height="1175" alt="Untitled (1)" src="https://github.com/user-attachments/assets/2b8e228a-2247-404e-a586-c85201687712" />





