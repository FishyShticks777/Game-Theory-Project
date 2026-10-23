#import numpy as np
import os

class Defector:
    def Defect(self):
        return "D"

class Cooperator:        
    def Cooperate(self, round, last_move_from_opponent="C"):
        if round == 1:
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
    p2_choice = "C"
    
    neighborhood1 = [[Cooperator(), Cooperator(), Cooperator(), Cooperator(), Cooperator()],
                    [Cooperator(), Cooperator(), Cooperator(), Cooperator(), Cooperator()],
                    [Cooperator(), Cooperator(), Defector(), Cooperator(), Cooperator()],
                    [Cooperator(), Cooperator(), Cooperator(), Cooperator(), Cooperator()],
                    [Cooperator(), Cooperator(), Cooperator(), Cooperator(), Cooperator()]]
                 
    for i in range(rounds):
        if i == 0:
            p1_choice = neighborhood1[2][1].Cooperate(1)
        else: 
            p1_choice = neighborhood1[2][1].Cooperate(rounds +1, p2_choice)
        p2_choice = neighborhood1[2][2].Defect()
        
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
        
    print(f"{p1_move_log}\n\n{p2_move_log}")
    print(f"\nPlayer 1 Points: {p1_points}\nPlayer 2 Points: {p2_points}")
        
PlayGame()
    
