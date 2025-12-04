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
| Integrasi  | Transfer Status Data                 | Pakai get_status(). Mengemas semua data penting (skor, nama, giliran) dalam bentuk dictionary untuk dikonsumsi oleh GUI.          
|              | Reset Backend              | Pakai reset_game(). Hanya membersihkan self.papan dan mengatur ulang self.pemain_saat_ini = 'X'.             
| Antarmuka (GUI)  | Input Nama Pemain                 |Method: _get_player_names(). Menggunakan simpledialog.askstring untuk mendapatkan input di awal.           
|              | Konstruksi GUI Papan              | Method: _setup_gui(). Membuat 9 instance tk.Button dan meletakkannya menggunakan grid di dalam self.frame_papan.             
|          | Penanganan Klik                  | Method: _klik_tombol(nomor_kotak). Memanggil backend.lakukan_gerakan() dan menggunakan return value untuk update tampilan.                
|           |Visualisasi Kemenangan                  | Method: _gambar_garis_kemenangan(combo). Menggunakan self.canvas_overlay.create_line() setelah kemenangan terdeteksi.   
|           | Pembaruan Tampilan Skor                 | Method: _update_score_display() dan _update_status_display(). Menggunakan data dari backend.get_status() untuk mengkonfigurasi teks tk.Label.          
|              | Fungsi Reset Frontend              | Method:_mulai_ulang(). Memanggil backend.reset_game() lalu menjalankan loop untuk mengatur ulang text dan state setiap tombol.


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

 ### *Flowchart GUI*
<img width="3232" height="1403" alt="Untitled" src="https://github.com/user-attachments/assets/2aa11920-191a-44e8-8ec0-eeeabd87bc7a" />

 ### *Penjelasan Flowchart*
1. Fase Inisialisasi dan Siaga

Siklus dimulai dari Frontend. Setelah program dieksekusi, ia segera meminta Input Nama Pemain. Data nama ini kemudian digunakan oleh Frontend untuk membuat objek Backend (TicTacToeBackend). Setelah objek Backend dibuat, Frontend memanggil Setup GUI (_setup_gui), membangun semua elemen visual (9 tombol, label skor, dll.), dan mengakhiri fase ini dengan memasuki Event Loop (mainloop), di mana ia menunggu aksi pengguna.

3. Fase Penanganan Aksi Pengguna (Frontend Aktif)
Program berada dalam mode siaga hingga terjadi salah satu dari dua aksi:
- Aksi Reset: Jika pengguna mengklik Tombol Reset, Frontend memanggil method reset_game() pada Backend (untuk membersihkan data logika), diikuti oleh pembersihan visual (mengosongkan tombol dan menghapus garis kemenangan) sebelum kembali ke Event Loop.
- Aksi Klik Tombol Papan: Ini adalah pemicu utama. Frontend menangkap klik dan memanggil backend.lakukan_gerakan(i), mengirimkan indeks kotak yang diklik.

3. Fase Pemrosesan Logika (Backend Reaktif)
Backend mengambil alih dengan method lakukan_gerakan.
- Validasi Gerakan: Backend pertama kali memeriksa apakah gerakan itu Valid (yaitu, apakah game_aktif adalah True dan kotak yang diklik masih Kosong).
- Jika Tidak Valid: Backend segera mengakhiri proses dan mengembalikan None, dan Frontend mengabaikan klik tersebut.
- Jika Valid: Backend mencatat simbol pemain pada papan (self.papan[i] = Simbol).
- Cek Hasil: Backend menjalankan cek_menang(). Jika ada hasil (Menang/Seri), ia memperbarui Skor dan mengatur game_aktif = False. Jika belum selesai, ia menjalankan proses Ganti Giliran Pemain.
- Akhir Backend: Backend mengembalikan status lengkap permainan (Simbol, Status, Kombinasi Kemenangan) ke Frontend.

4. Fase Visualisasi Hasil (Frontend Memperbarui)

Frontend menerima data dari Backend dan menggunakannya untuk memperbarui tampilan secara spesifik:

Update Tombol: Frontend selalu memperbarui tampilan tombol yang baru diklik (teks simbol dan warna X/O) dan menonaktifkannya (state=DISABLED).

Visualisasi Akhir Ronde:
- Jika status adalah Menang/Seri, Frontend memanggil _update_score_display, menggunakan method _gambar_garis_kemenangan (jika menang), dan menampilkan Pesan Pop-up (messagebox).
- Jika status Lanjut, Frontend hanya memanggil _update_status_display untuk menunjukkan giliran pemain berikutnya.

Kembali ke Siklus: Setelah semua pembaruan visual selesai, alur kembali ke Event Loop, siap menerima aksi berikutnya.
