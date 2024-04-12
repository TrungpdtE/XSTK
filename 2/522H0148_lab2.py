
from fractions import Fraction

def P(event , space):
  return Fraction(len(event & space) ,  len(space))

D={1,2,3,4,5,6}
even={2,4,6}

print(P(even,D))

#Omega
import itertools

def cross(A,B):
  return {a+b for a in A for b in B}

urn=cross('W','12345678') | cross('B','123456') | cross('R','123456789')
print(urn)
print("---------------- \n")
def combos(item,n):
  return {' '.join(combo) for combo in itertools. combinations(item,n)}

U6=combos(urn,6)

print(len(U6))
print("---------------- \n")

#Take 10 random subsets from set U6.
import random

print(random.sample(U6,10))
print("---------------- \n")

#Problem 1: All 6 balls are red
red6 = {s for s in U6 if s.count('R') ==6}

print("Problem 1: All 6 balls are red \n")
print(red6,U6)
print("-------------\n")

#Problem 2: 3 blue , 2 white and 1 red
b3w2r1 = {s for s in U6 if s.count('B') ==3 and s.count('W') == 2 and s.count('R') ==1}
print("3 blue , 2 white and 1 red \n")
print(b3w2r1,U6)
print("------------\n")

#Problem 3: 4 white
w4 ={s for s in U6 if s.count('W') ==4}
print("Exactly 4 white ball \n")
print(w4,U6)
print("-----------------\n")

#coin experiment
import random
n=1000000
count = 0
for simulations in range(n):
  tosses = random.randint(0,1)
  if tosses ==1:
    count+=1

print(count /n)

#dices experiment
import random
count=0
n=1000000
for i in range(n):
  die1=random.randint(1,6)
  die2=random.randint(1,6)
  if die1==1 and die2 ==6:
    count+=1
print(count/n)

from itertools import product
import random

#define ranks, suits, and cards
ranks = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'J', 'Q', 'K'}
suits = {'co', 'ro', 'chuon', 'bich'}
cards = list(product(ranks, suits))
print(len(cards))
print(cards[:10])

# red cards
def simulator_poker(n):
    count = 0
    for i in range(n):
        index = random.randint(0, 51)
        if cards[index][1] == 'co' or cards[index][1] == 'ro':
            count += 1
    return count / n

# main
print(simulator_poker(1000000))

#ex1
import random

def simulator_dice1(n):
    count = 0
    even = {2, 4, 6}
    for _ in range(n):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        if die1 in even and die2 in even:
            count += 1
    return count / n

# main
n = 100000
print(simulator_dice1(n))

#ex2
import random

def simulator_dice2(n):
  count=0
  even={2,4,6}
  odd={1,3,5}
  for _ in range(n):
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    if die1 in odd and die2 in even:
      count+=1
  return count/n

#main
n=100000
print(simulator_dice2(n))

#ex3
import random

def simulator_dice3(n):
  count=0
  for _ in range(n):
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    if die1 == die2:
      count+=1
  return count/n

#main
n=100000
print(simulator_dice3(n))

#ex4
import random

def simulator_dice4(n):
  count=0
  for _ in range(n):
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    if die1 == 1 and die2 == 6:
      count+=1
  return count/n

#main
n=100000
print(simulator_dice4(n))

#ex5
import random

def simulator_dice3(n):
  count=0
  for _ in range(n):
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    if die1+die2 >6:
      count+=1
  return count/n

#main
n=100000
print(simulator_dice3(n))

#ex6
from itertools import product
import random

# Define ranks, suits, and cards
ranks = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'}
suits = {'♡', '♢', '♣', '♠'}
cards = list(product(ranks, suits))
print(len(cards))
print(cards[:10])

def simulator_poker1(n):
    count = 0
    for _ in range(n):
        hand = random.sample(cards, 5)
        is_all_hearts = all(card[1] == '♡' for card in hand)
        if is_all_hearts:
            count += 1
    return count / n

print(simulator_poker1(1000000))

#ex7
from itertools import product
import random

# Define ranks, suits, and cards
ranks = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'}
suits = {'♡', '♢', '♣', '♠'}
cards = list(product(ranks, suits))
print(len(cards))
print(cards[:10])

def simulator_poker2(n):
    count = 0
    for _ in range(n):
        hand = random.sample(cards, 4)
        is_all= len(set(hand)) == 4
        if is_all:
            count += 1
    return count / n

print(simulator_poker2(100000))

#ex8
import random
import itertools

def cross(A, B):
  return {a + b for a in A for b in B}
urn = cross('W', '12345678') | cross('B', '123456') | cross('R', '123456789')

print(urn)

def simulator_balls(n):
    count = 0
    for _ in range(n):
        hand = random.sample(urn, 6)
        is_ball= len(set(hand)) == 3
        if is_ball:
            count += 1
    return count / n

print(simulator_balls(1000))