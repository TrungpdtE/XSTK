#EX1

import itertools
print("\ncau 1: \n")
A={1,2,3,4,5}
k=3
permute_k = list(itertools.permutations(A, k))
n=len(permute_k)
print("Number of the Num 3 digit:",n )
print("\n", permute_k )
for i in permute_k:
  print(i)


#EX2

import itertools
print("\ncau 2: \n")
def cross(A, B):
  return {a + b for a in A for b in B}
urn = cross('W', '12345678') | cross('B', '123456') | cross('R', '123456789')
#print(urn)

U3=list(itertools.combinations(urn,3))
print(U3)
len_U3=len(U3)
print(len_U3)

dem=0
for i in U3:
  if(i[1][0]!=i[0][0] and i[0][0]!=i[2][0] and i[1][0]!=i[2][0]):
    dem=dem+1

print(dem)


dem1=0
for i in U3:
  if(i[0][0]=='W' and i[1][0]=='R'):
    dem1=dem1+1
print(dem1)




#EX3
import itertools
print("\ncau 3: \n")
def cross(A,B):
  return {a+b for a in A for b in B}
urn = cross('M', '1234') | cross('P', '123') | cross('C', '12') | cross('E','1')
#print(urn)

U4=list(itertools.permutations(urn,10))
k=0
len_U4=len(U4)
print(len_U4)
for i in U4:

  count=0
  if(i[1][0]!=i[2][0]):
    count=count+1
  if(i[2][0]!=i[3][0]):
    count=count+1
  if(i[3][0]!=i[4][0]):
    count=count+1
  if(i[4][0]!=i[5][0]):
    count=count+1
  if(i[5][0]!=i[6][0]):
    count=count+1
  if(i[6][0]!=i[7][0]):
    count=count+1
  if(i[7][0]!=i[8][0]):
    count=count+1
  if(i[8][0]!=i[9][0]):
    count=count+1
  if(i[0][0]!=i[1][0]):
    count=count+1
  if(count==3):
    k=k+1
print(k)
print(len_U4)


#EX4
import itertools
print("\ncau 4: \n")

def cross(A,B):
  return {a+b for a in A for b in B}
urn = cross('M', '123456') | cross('W', '123456789')
#print(urn)

U4=list(itertools.combinations(urn,5))
k=0

len_U4=len(U4)
print(len_U4)

for i in U4:
  count=0
  if(i[0][0]=='W'):
    count=count+1
  if(i[1][0]=='W'):
    count=count+1
  if(i[2][0]=='W'):
    count=count+1
  if(i[3][0]=='W'):
    count=count+1
  if(i[4][0]=='W'):
    count=count+1
  if(count==2):
    k=k+(100000*2*5-999999)*33-16*2
print(k)

#EX5
print('"câu 5')
import itertools 
from itertools import product, combinations

def cross(A, B):   
    return {a+b for a in A for b in B} 

A = (1, 2, 3, 4 ,5 ,6 , 7, 8, 9, 10, 'J', 'Q', 'K')
B = ('♠', '♣', '♦' ,'♥') 

Card = list(product(A, B)) 
poker_5 = list(combinations(Card, 5)) 
len_poker_5 = len(poker_5) 
print(len_poker_5) 

three_of_a_kind = []
len_three_of_a_kind = 0 

for hand in poker_5:   
    count = 0   
    values = [card[0] for card in hand]
    for value in values:
        if values.count(value) == 3:
            count += 1
            values = [v for v in values if v != value]
            break
    if count == 1 and len(set(values)) == 2:
        three_of_a_kind.append(hand)
        len_three_of_a_kind += 1

print(len_three_of_a_kind)