import tkinter as tk
from tkinter import messagebox


class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe")
        self.current_player = 'X'
        self.create_board()

    def create_board(self):
        self.buttons = [[None] * 3 for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.master, width=10, height=4,
                                               font=('Arial', 20, 'bold'),
                                               command=lambda row=i, col=j: self.on_click(row, col))
                self.buttons[i][j].grid(row=i, column=j)

    def on_click(self, row, col):
        if self.buttons[row][col]['text'] == '':
            self.buttons[row][col]['text'] = self.current_player
            if self.check_winner(row, col):
                messagebox.showinfo("Tic Tac Toe", f"Player {self.current_player} wins!")
                self.reset_board()
            elif self.check_draw():
                messagebox.showinfo("Tic Tac Toe", "It's a draw!")
                self.reset_board()
            else:
                self.switch_player()

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'
        # Change color for the second player (O)
        if self.current_player == 'O':
            for i in range(3):
                for j in range(3):
                    self.buttons[i][j].configure(bg='lightblue')
        else:
            for i in range(3):
                for j in range(3):
                    self.buttons[i][j].configure(bg='SystemButtonFace')

    def check_winner(self, row, col):
        # Check row
        if (self.buttons[row][0]['text'] == self.buttons[row][1]['text'] == self.buttons[row][2][
            'text'] == self.current_player):
            return True
        # Check column
        if (self.buttons[0][col]['text'] == self.buttons[1][col]['text'] == self.buttons[2][col][
            'text'] == self.current_player):
            return True
        # Check diagonal
        if (row == col and self.buttons[0][0]['text'] == self.buttons[1][1]['text'] == self.buttons[2][2][
            'text'] == self.current_player):
            return True
        # Check reverse diagonal
        if (row + col == 2 and self.buttons[0][2]['text'] == self.buttons[1][1]['text'] == self.buttons[2][0][
            'text'] == self.current_player):
            return True
        return False

    def check_draw(self):
        for i in range(3):
            for j in range(3):
                if self.buttons[i][j]['text'] == '':
                    return False
        return True

    def reset_board(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j]['text'] = ''
                self.buttons[i][j].configure(bg='SystemButtonFace')
        self.current_player = 'X'


if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
