class Connect_4:
    
    def __init__(self):
        self.board = [[' ' for _ in range(8)] for _ in range(8)]
        self.turns = 0

    def show_board(self):
        # Un espacio
        print('\n')

        # Fila que lista las columnas
        for col in range(8):                
            print(f'  ({col+1}) ', end = '')
        print('\n')                                
        
        # Matriz del tablero de juego, ordenada estéticamente
        for row in range(8):                
            print('|', end = '')
            for col in range(8):                                   
                print(f'  {self.board[row][col]}  |', end = '')
            print('\n')

    def player_turn(self):
        players = ['1', '2']
        return players[self.turns % 2]

    def put_token(self, col):
        col = col-1
        for row in range(7, -1, -1):
            if self.board[row][col] == ' ':
                self.board[row][col] = self.player_turn()
                self.turns += 1
                return True

    def winner(self):
    # Revisar Horizontales
        for row in range(8):
            for col in range(5):
                if(
                     self.board[row][col] != ' ' and 
                     self.board[row][col] == self.board[row][col+1] == self.board[row][col+2] == self.board[row][col+3]
                ):
                    return (f'El Jugador {self.board[row][col]} ganó con 4 en Horizontal')

	# Revisar Verticales
        for row in range(5):
            for col in range(8):
                if( 
                    self.board[row][col] != ' ' and
                    self.board[row][col] == self.board[row+1][col] == self.board[row+2][col] == self.board[row+3][col]
                ):
                    return (f'El Jugador {self.board[row][col]} ganó con 4 en Vertical')

	# Revisar Diagonal Izquierda
        for row in range(5):
            for col in range(5):
                if(
                    self.board[row][col] != ' ' and 
                    self.board[row][col] == self.board[row+1][col+1] == self.board[row+2][col+2] == self.board[row+3][col+3]
                ):
                    return (f'El Jugador {self.board[row][col]} ganó con 4 en Diagonal Negativa')

	# Revisar Diagonal Derecha
        for row in range(5):
            for col in range(3, 8):
                if( self.board[row][col] != ' ' and 
                    self.board[row][col] == self.board[row+1][col-1] == self.board[row+2][col-2] == self.board[row+3][col-3]
                ):
                    return (f'El Jugador {self.board[row][col]} ganó con 4 en Diagonal Positiva')
            
        if not any(' ' in _ for _ in self.board):
            return('Empate')
                    
	# No hay ganador aún       
        return True