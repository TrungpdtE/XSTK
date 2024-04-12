from fractions import Fraction
import random
import itertools

def P(event , space):
    return Fraction(len(event & space), len(space))
#cau1
S = {'MMM', 'MMF', 'MFM', 'FFF'}

B = {s for s in S if 'F' in s}
A = {s for s in B if s.count('F')==3}

P_B = P(B, S)
P_A_B = P(A, S)

P_A_with_B = P_A_B/P_B
print(P_A_with_B)
S = {'MMM', 'MMF', 'MFM', 'MFF', 'FMM', 'FMF', 'FFM', 'FFF'}

num_elements_S = len(S)
print(num_elements_S)

B = {s for s in S if 'F' in s}
print(B)

A = {s for s in S if s == 'FFF'}
print(A)

P_B = P(B, S)
P_A_B = P(A, S)
P_A_with_B = P_A_B/P_B
print(P_A_with_B)


#cau2
def P(event , space):
    return Fraction(len(event), len(space))
S = [('Thanh', 'Nữ'), ('Hồng', 'Nữ'), ('Thương', 'Nữ'), ('Đào', 'Nữ'), ('My', 'Nữ'), ('Yến', 'Nữ'), ('Hạnh', 'Nữ'),
      ('My', 'Nữ'), ('Vy', 'Nữ'), ('Tiên', 'Nữ'), ('Thanh', 'Nam'), ('Thanh', 'Nam'), ('Bình', 'Nam'), ('Nhật', 'Nam'),
      ('Hào', 'Nam'), ('Đạt', 'Nam'), ('Minh', 'Nam')]
      
A = [s for s in S if s[0] == 'Thanh']
B = [s for s in S if s[1] == 'Nữ']
A_B = [s for s in A if s in B]

P_A = P(A, S)
P_B = P(B, S)
P_A_B = P(A_B, S)
P_Thanh_given_female = P(A_B, B)

print(P_A)
print(P_B)
print(P_A_B)
print(P_Thanh_given_female)

#cau3
import random
from fractions import Fraction

def P(event , space):
    return len(event) / len(space)
def combos(items , n):
    return {' '.join(combo) for combo in itertools.
    combinations(items , n)}

suits = ['♠', '♡', '♢', '♣']
ranks = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
Cards = {rank + suit for suit in suits for rank in ranks}
B = combos(Cards, 3)

A1 = {card for card in B if card.count('K') == 1 or card.count('K') == 2 }
A2 = {card for card in B if 'K' in card}

P_A1 = P(A1, B)
P_A2 = P(A2, B)

print(P_A1)
print(P_A2)
