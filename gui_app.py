import tkinter as tk
from functools import partial

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
        
