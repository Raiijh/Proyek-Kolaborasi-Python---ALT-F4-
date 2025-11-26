import tkinter as tk
from functools import partial
from tkinter import messagebox, simpledialog
from tictactoe_game import TicTacToeBackend

# Warna Custom
BG_COLOR = "#2a3d66" 
BUTTON_COLOR = "#0f1a30"
X_COLOR = "#ffd700" 
O_COLOR = "#c084fc"
TITLE_BAR_COLOR = "#e76f51" 
TEXT_COLOR = "#ffffff" 
WIN_LINE_COLOR = "#00ff00" 

PADDING = 5 
BUTTON_WIDTH_CHARS = 4
BUTTON_HEIGHT_LINES = 2


class TicTacToeGUI:
    def __init__(self, root):
        """
        Menginisialisasi jendela Tkinter dan menyiapkan Backend.
        
        Args:
            root (tk.Tk): Objek root window Tkinter.
        
        """
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
        """Meminta pemain untuk menginput nama.
        
        Returns:
            dict: Kamus nama pemain dengan kunci 'X' dan 'O'.
        
        """
        name_x = simpledialog.askstring("Input Nama", "Masukkan Nama Pemain X:", initialvalue="Player 1")
        name_o = simpledialog.askstring("Input Nama", "Masukkan Nama Pemain O:", initialvalue="Player 2")
        
        return {
            'X': name_x if name_x else "Pemain X",
            'O': name_o if name_o else "Pemain O"
        }

    def _update_score_display(self):
        """Memperbarui teks pada skor."""
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
        """Menggambar garis kemenangan secara akurat.
        
        Args:
            nomor_kotak (int): Indeks 0-8 dari tombol yang dihitung.
            
        Returns:
            tuple: Koordinat (x, y) pusat tombol."""
        
        self.root.update_idletasks() 
        tombol = self.tombol_list[nomor_kotak]
        x = tombol.winfo_x() + tombol.winfo_width() / 2
        y = tombol.winfo_y() + tombol.winfo_height() / 2
        return x, y

    def _gambar_garis_kemenangan(self, combo):
        """Menggambar garis saat salah satu pemain menang.
        
        Args:
            combo (tuple): Tuple yang berisi tiga indeks kotak pemenang (misal: (0, 4, 8)).
        
        """
        if self.canvas_line:
            self.canvas_overlay.delete(self.canvas_line)

        x1, y1 = self._hitung_pusat_tombol(combo[0])
        x2, y2 = self._hitung_pusat_tombol(combo[2])
        
        self.canvas_line = self.canvas_overlay.create_line(x1, y1, x2, y2, 
                                                fill=WIN_LINE_COLOR, width=8, tags="win_line")
        self.canvas_overlay.lift(self.canvas_line)

    def _klik_tombol(self, nomor_kotak):
        """Fungsi yang dipanggil saat diklik.
        
        Args:
            nomor_kotak (int): Indeks tombol yang diklik.
        
        """
        
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

    def _mulai_ulang(self):
        """
        Mereset status game.
        """
        self.backend.reset_game()
        self._update_status_display()
        
        for tombol in self.tombol_list:
            tombol.config(text="", state=tk.NORMAL, bg=BUTTON_COLOR, fg=TEXT_COLOR, relief=tk.FLAT)
        
        if self.canvas_line:
            self.canvas_overlay.delete(self.canvas_line)
            self.canvas_line = None

    def _setup_gui(self):
        """
        Membangun dan mengatur semua elemen visual Tkinter: 
        header, label skor, frame papan, tombol, dan tombol reset.
        """
        self.root.title("Tic-Tac-Toe Game")
        self.root.configure(bg=BG_COLOR) 

        # Header Frame
        header_frame = tk.Frame(self.root, bg=TITLE_BAR_COLOR, height=80)
        header_frame.pack(fill=tk.X, pady=(0, 20)) 
        header_frame.pack_propagate(False)

        tk.Label(header_frame, text="TIC-TAC-TOE GAME", font=('Arial', 24, 'bold'), fg=TEXT_COLOR, bg=TITLE_BAR_COLOR).pack(pady=(10, 0))
        tk.Label(header_frame, text="Kelompok ALT-F4", font=('Arial', 10), fg=TEXT_COLOR, bg=TITLE_BAR_COLOR).pack()
        
        self.label_score = tk.Label(self.root, font=('Arial', 14), fg=TEXT_COLOR, bg=BG_COLOR)
        self.label_score.pack(pady=(0, 10))

        self.frame_papan = tk.Frame(self.root, bg=BG_COLOR) 
        self.frame_papan.pack(pady=10, padx=20) 

        self.canvas_overlay = tk.Canvas(self.frame_papan, bg=BG_COLOR, highlightthickness=0, borderwidth=0)
        self.canvas_overlay.place(relx=0, rely=0, relwidth=1, relheight=1)
        
        self.frame_papan.grid_columnconfigure((0, 1, 2), weight=1)
        self.frame_papan.grid_rowconfigure((0, 1, 2), weight=1)

        for i in range(9):
            baris = i // 3
            kolom = i % 3
            tombol = tk.Button(self.frame_papan, text="", font=('Arial', 36, 'bold'), width=BUTTON_WIDTH_CHARS, height=BUTTON_HEIGHT_LINES, bd=0, bg=BUTTON_COLOR, fg="lightgray", activebackground=BUTTON_COLOR, activeforeground="lightgray", relief=tk.FLAT, command=partial(self._klik_tombol, i))
            tombol.grid(row=baris, column=kolom, padx=PADDING, pady=PADDING, sticky="nsew")
            self.tombol_list.append(tombol)

        for tombol in self.tombol_list:
            tombol.lift()

        self.label_status = tk.Label(self.root, font=('Arial', 16, 'bold'), fg=TEXT_COLOR, bg=BG_COLOR)
        self.label_status.pack(pady=20)
        self._update_status_display() 

        tombol_reset = tk.Button(self.root, text="Mulai Ulang", font=('Arial', 14, 'bold'), bg=TITLE_BAR_COLOR, fg=TEXT_COLOR, activebackground=TITLE_BAR_COLOR, activeforeground=TEXT_COLOR, padx=15, pady=8, bd=0, relief=tk.FLAT, command=self._mulai_ulang)
        tombol_reset.pack(pady=10)

if __name__ == "__main__":
    """
    Blok eksekusi utama: Menjalankan aplikasi GUI dan membuat instance root Tkinter.
    """
    root = tk.Tk()
    app = TicTacToeGUI(root)
    root.mainloop()
