#import numpy as np
import os

class Defector:
    def Play(self, round, last_move_from_opponent=""):
        return "D"

class Cooperator:        
    def Play(self, round, last_move_from_opponent=""):
        if round == 0:
            return "C"
        if last_move_from_opponent == "C":
            return "C"
        else:
            return "D"
    

def PlayGame():
    rounds = 20
    p1_points = 0
    p2_points = 0
    p1_move_log = "Player 1 moves:"
    p2_move_log = "Player 2 moves:"
    
    neighborhood1 = [[Cooperator(), Cooperator(), Cooperator(), Cooperator(), Cooperator()],
                    [Cooperator(), Cooperator(), Cooperator(), Cooperator(), Cooperator()],
                    [Cooperator(), Cooperator(), Defector(), Cooperator(), Cooperator()],
                    [Cooperator(), Cooperator(), Cooperator(), Cooperator(), Cooperator()],
                    [Cooperator(), Cooperator(), Cooperator(), Cooperator(), Cooperator()]]

    # neighborhood2 = [[Defector(), Defector(), Defector(), Defector(), Defector()],
    #                  [Defector(), Defector(), Defector(), Defector(), Defector()],
    #                  [Defector(), Defector(), Cooperator(), Defector(), Defector()],
    #                  [Defector(), Defector(), Defector(), Defector(), Defector()],
    #                  [Defector(), Defector(), Defector(), Defector(), Defector()]]
    for row in range(5):
        for column in range(5):

            for row_offset in (-1, 0, 1):
                for column_offset in (-1, 0, 1):


                    if row_offset == 0 and column_offset == 0:
                        continue

                    neighbor_row = row + row_offset
                    neighbor_column = column + column_offset

                    if 0 <= neighbor_row < 5 and 0 <= neighbor_column < 5:
                        if (neighbor_row, neighbor_column) > (row, column):
                            p1_points = 0
                            p2_points = 0
                            p1_move_log = "Player 1 moves:"
                            p2_move_log = "Player 2 moves:"

                            for i in range(rounds):
                                if i == 0:
                                    p1_choice = neighborhood1[row][column].Play(i)
                                    p2_choice = neighborhood1[neighbor_row][neighbor_column].Play(i)
                                else:
                                    p1_choice = neighborhood1[row][column].Play(rounds, p2_past_choice)
                                    p2_choice = neighborhood1[neighbor_row][neighbor_column].Play(rounds, p1_past_choice)
                                
                                p1_move_log += f" {p1_choice} "
                                p2_move_log += f" {p2_choice} "
                                
                                if p1_choice == "C" and p2_choice == "C":
                                    p1_points +=3
                                    p2_points +=3
                                elif p1_choice == "D" and p2_choice == "C":
                                    p1_points +=5
                                elif p1_choice == "C" and p2_choice == "D":
                                    p2_points+=5
                                else:
                                    p1_points +=1
                                    p2_points +=1

                                p1_past_choice = p1_choice
                                p2_past_choice = p2_choice

                            print(f"\n{p1_move_log}\n\n{p2_move_log}")
                            print(f"\nPlayer 1 Points: {p1_points}\nPlayer 2 Points: {p2_points}")
        
PlayGame()
    
