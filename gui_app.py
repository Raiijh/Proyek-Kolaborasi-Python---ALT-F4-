import tkinter as tk
from functools import partial
from tictactoe_game import TicTacToeBackend

# --- Warna Custom ---
BG_COLOR = "#2a3d66" 
BUTTON_COLOR = "#0f1a30"
X_COLOR = "#ffd700" 
O_COLOR = "#c084fc"
TITLE_BAR_COLOR = "#e76f51" 
TEXT_COLOR = "#ffffff" 
WIN_LINE_COLOR = "#00ff00" 

# Ukuran untuk perhitungan visual
PADDING = 5 
BUTTON_WIDTH_CHARS = 4
BUTTON_HEIGHT_LINES = 2


class TicTacToeGUI:
    def __init__(self, root):
        self.root = root
        self.tombol_list = []
        self.canvas_line = None
        
        # Inisialisasi Nama & Backend
        self.player_names = self._get_player_names()
        self.backend = TicTacToeBackend(self.player_names) 

        self._setup_gui()
        self._update_score_display()

    #Fungsi Utility (Update Tampilan dan Koordinat)
    def _get_player_names(self):
        """Meminta nama pemain menggunakan simpledialog."""
        name_x = simpledialog.askstring("Input Nama", "Masukkan Nama Pemain X:", initialvalue="Player 1")
        name_o = simpledialog.askstring("Input Nama", "Masukkan Nama Pemain O:", initialvalue="Player 2")
        
        return {
            'X': name_x if name_x else "Pemain X",
            'O': name_o if name_o else "Pemain O"
        }

    def _update_score_display(self):
        """Memperbarui teks pada label skor."""
        status = self.backend.get_status()
        names = status['names']
        scores = status['scores']
        score_text = f"{names['X']} (X): {scores['X']} | {names['O']} (O): {scores['O']}"
        self.label_score.config(text=score_text)

    def _update_status_display(self):
        """Memperbarui teks giliran pemain."""
        status = self.backend.get_status()
        nama_saat_ini = status['nama_saat_ini']
        player_saat_ini = status['player_saat_ini']
        self.label_status.config(text=f"Giliran: {nama_saat_ini} ({player_saat_ini})", fg=TEXT_COLOR)
    
    def _hitung_pusat_tombol(self, nomor_kotak):
        """Menghitung koordinat pusat tombol yang tepat untuk Canvas."""
        self.root.update_idletasks() 
        tombol = self.tombol_list[nomor_kotak]
        x = tombol.winfo_x() + tombol.winfo_width() / 2
        y = tombol.winfo_y() + tombol.winfo_height() / 2
        return x, y

    def _gambar_garis_kemenangan(self, combo):
        """Menggambar garis kemenangan di atas Canvas."""
        if self.canvas_line:
            self.canvas_overlay.delete(self.canvas_line)

        x1, y1 = self._hitung_pusat_tombol(combo[0])
        x2, y2 = self._hitung_pusat_tombol(combo[2])
        
        self.canvas_line = self.canvas_overlay.create_line(x1, y1, x2, y2, 
                                                fill=WIN_LINE_COLOR, width=8, tags="win_line")
        self.canvas_overlay.lift(self.canvas_line)

    def _klik_tombol(self, nomor_kotak):
        """Menangani event klik tombol. Berinteraksi dengan Backend."""
        
        # Panggil Backend untuk memproses gerakan
        pemain_symbol, hasil, combo = self.backend.lakukan_gerakan(nomor_kotak)
        
        if pemain_symbol:
            tombol = self.tombol_list[nomor_kotak] 
            tombol.config(text=pemain_symbol, state=tk.DISABLED, 
                          fg=X_COLOR if pemain_symbol == 'X' else O_COLOR,
                          bg=BUTTON_COLOR, 
                          relief=tk.FLAT)

            if hasil == "Seri":
                messagebox.showinfo("Game Selesai", "Permainan Berakhir SERI!")
            
            elif hasil and hasil != "Seri":
                self._update_score_display()
                self._gambar_garis_kemenangan(combo) 
                pemenang_nama = self.backend.player_names[hasil]
                messagebox.showinfo("Game Selesai", f"🎉 Selamat! {pemenang_nama} ({hasil}) MENANG!")
            
            if self.backend.game_aktif:
                 self._update_status_display()
