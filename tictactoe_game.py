class TicTacToeBackend:
    def __init__(self, player_names):
        """status awal game dan data pemain."""
        self.papan = [""] * 9
        self.pemain_saat_ini = 'X'
        self.game_aktif = True
        
        self.player_names = player_names
        self.scores = {'X': 0, 'O': 0}
        
        self.menang_kombinasi = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6)
        ]

    def cek_menang(self):
        """Mengecek kemenangan."""
        for combo in self.menang_kombinasi:
            a, b, c = combo
            if self.papan[a] == self.papan[b] == self.papan[c] and self.papan[a] != "":
                self.game_aktif = False
                return self.papan[a], combo
        
        if "" not in self.papan:
            self.game_aktif = False
            return "Seri", None
            
        return None, None
    
    def lakukan_gerakan(self, nomor_kotak):
        """Melakukan gerakan, memperbarui skor jika menang, dan mengganti pemain."""
        if not self.game_aktif or self.papan[nomor_kotak] != "":
            return None, None, None

        pemain = self.pemain_saat_ini
        self.papan[nomor_kotak] = pemain
        
        hasil, combo = self.cek_menang()

        if hasil and hasil != "Seri":
            self.scores[hasil] += 1
            
        if self.game_aktif:
            self.pemain_saat_ini = 'O' if pemain == 'X' else 'X'
            
        return pemain, hasil, combo
    
    def reset_game(self):
        """Mempersiapkan papan untuk ronde baru."""
        self.papan = [""] * 9
        self.game_aktif = True
        self.pemain_saat_ini = 'X' 
        
    def get_status(self):
        """Mengembalikan data status game."""
        return {
            'player_saat_ini': self.pemain_saat_ini,
            'nama_saat_ini': self.player_names[self.pemain_saat_ini],
            'scores': self.scores,
            'names': self.player_names
        }