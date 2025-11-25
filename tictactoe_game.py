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