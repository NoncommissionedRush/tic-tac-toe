import time
class TicTacToe():

    moves = 0
    round = 0
    game_on = True
    player_turns = []
    computer_turns = []
    player_score = 0
    computer_score = 0

    cells = {
        "a1": " ",
        "a2": " ", 
        "a3": " ", 
        "b1": " ",
        "b2": " ",
        "b3": " ",
        "c1": " ",
        "c2": " ",
        "c3": " "
    }
    
    winning_combinations = [
        ['a1', 'a2', 'a3'], 
        ['b1', 'b2', 'b3'], 
        ['c1', 'c2', 'c3'], 
        ['a1', 'b1', 'c1'], 
        ['a2', 'b2', 'c2'], 
        ['a3', 'b3', 'c3'], 
        ['a1', 'b2', 'c3'], 
        ['a3', 'b2', 'c1']
    ]

    board = f"""
    a     b     c
       |     |     
1   {cells['a1']}  |  {cells['b1']}  |  {cells['c1']}  
  _____|_____|_____
       |     |     
2   {cells['a2']}  |  {cells['b2']}  |  {cells['c2']}  
  _____|_____|_____
       |     |     
3   {cells['a3']}  |  {cells['b3']}  |  {cells['c3']}  
       |     |     

    """


    def update_board(self):
        self.board =  f"""
    a     b     c
       |     |     
1   {self.cells['a1']}  |  {self.cells['b1']}  |  {self.cells['c1']}  
  _____|_____|_____
       |     |     
2   {self.cells['a2']}  |  {self.cells['b2']}  |  {self.cells['c2']}  
  _____|_____|_____
       |     |     
3   {self.cells['a3']}  |  {self.cells['b3']}  |  {self.cells['c3']}  
       |     |     

   """ 


    def player_turn(self):
        player_input =  input("Type a/b/c for column and 1/2/3 for row: ")
        try:
            if self.cells[player_input] == " ":
                self.cells[player_input] = "x"
                self.update_board()
                self.moves += 1
                self.player_turns.append(player_input)
            else:
                print("That cell has already been played")
        except KeyError:
            print("That cell does not exist")
    

    def check_if_two_in_line(self, turns):
        cell_to_play = None
        for combination in self.winning_combinations:
            if sum(value in combination for value in turns) >= 2:
                cell_to_play = [cell for cell in combination if cell not in self.player_turns][0]
                if self.cells[cell_to_play] == " ":
                    break
                else:
                    cell_to_play = None
        return cell_to_play

                    
    def computer_turn(self):
        cell_to_play = None
        if len(self.player_turns) >=2:
            cell_to_play = self.check_if_two_in_line(self.player_turns)

        if cell_to_play == None and len(self.computer_turns) >= 2:
            cell_to_play = self.check_if_two_in_line(self.computer_turns)

        if cell_to_play == None:
            if self.cells['b2'] == " " and self.round % 2 != 0:
                cell_to_play = 'b2'
            else:
                for cell in self.cells:
                    if self.cells[cell] == " ":
                        cell_to_play = cell 
                        break

        self.cells[cell_to_play] = "o"
        self.update_board()
        self.moves += 1 
        self.computer_turns.append(cell_to_play)
        return
        
    
    def check_win(self):
        for combination in self.winning_combinations:
            if sum(value in self.player_turns for value in combination) == 3:
                self.game_on = False
                print("YOU WIN!")
                self.player_score += 1
                return
            elif sum(value in self.computer_turns for value in combination) == 3:
                self.game_on = False
                print("COMPUTER WINS!")
                self.computer_score += 1
                return

        if self.moves == 8 + self.round:
            self.game_on = False
            print("It's a tie")
            return


    def play_game(self):
        print(self.board)
        self.round += 1

        while self.moves < 9 + self.round and self.game_on:
            if self.moves % 2 == 0:
                self.player_turn()
            else:
                time.sleep(1)
                self.computer_turn()
            print(self.board)
            if self.moves > 5:
                self.check_win()

        play_again = input("Play again? Y/N ")

        if play_again == "y":
            self.game_on = True
            self.moves = 0 + self.round
            self.player_turns = []
            self.computer_turns = []
            for cell in self.cells:
                self.cells[cell] = " "
            self.update_board()
            self.play_game()
        else:
            print("FINAL SCORE:")
            print(f"YOU: {self.player_score}")
            print(f"COMPUTER: {self.computer_score}")



tic_tac_toe = TicTacToe()

tic_tac_toe.play_game()