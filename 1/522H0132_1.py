import itertools
import math
#cau1
A=[1,2,3,4,5]
num_3_digit = []
choose_3 = itertools.permutations(A,3)
for permutation in choose_3:
    num_3_digit.append(int(''.join(map(str, permutation))))

num_lenght = len(num_3_digit)
print(num_3_digit)
print(num_lenght)

#cau2
def cross(A, B):
    return {a + b for a in A for b in B}

urn = cross('W', '12345678') | cross('B', '123456') | cross('R', '123456789')
U3 = list(itertools.combinations(urn, 3))
print(len(U3))
for i in U3:
    if i[0][0] == 'W' and i[-2][0] == 'B' and i[-1][0] == 'R' or i[0][0] == 'W' and i[-2][0] == 'R' and i[-1][0] == 'B' or i[0][0] == 'R' and i[-2][0] == 'W' and i[-1][0] == 'B' or i[0][0] == 'R' and i[-2][0] == 'B' and i[-1][0] == 'W' or i[0][0] == 'B' and i[-2][0] == 'W' and i[-1][0] == 'R' or i[0][0] == 'B' and i[-2][0] == 'R' and i[-1][0] == 'W' :
        print(i)
for s in U3:
    if s[0][0] == 'W' and s[-2][0] == 'R' and s[-1][0] == 'B':
        print(s)

#cau3:
def cross(A, B):
    return {a + b for a in A for b in B}

urn = cross('M', '1234') | cross('C', '12') | cross('P', '123') | cross('L', '1')

mathbook = cross('M', '1234')
mathways = list(itertools.permutations(mathbook))

chemicbooks = cross('C', '12')
chemicways = list(itertools.permutations(chemicbooks))

physicbooks = cross('P', '123')
physicways = list(itertools.permutations(physicbooks))

def print_arrangements():
    total = []
    for math_arrangement in mathways:
        for chemic_arrangement in chemicways:
            for physic_arrangement in physicways:
                arrangement = [math_arrangement] + [chemic_arrangement] + [physic_arrangement] + ['L1']
                result = list(itertools.permutations(arrangement))
                for i in result:
                    total.append(i)
    print(len(total))
    return total
a = print_arrangements()
for i in a:
    print(i)

#cau4
import itertools

def cross(A, B):
    return {a + b for a in A for b in B}

urn = cross('M', '123456') | cross('W', '123456789')

Men = cross('M', '123456')
Men_attend = list(itertools.combinations(Men,3))

Women = cross('W', '123456789')
Women_attend = list(itertools.combinations(Women,2))

def print_arrangements():
    total=[]
    for men_arrangement in Men_attend:
        for women_arrangement in Women_attend:
            arrangement = [men_arrangement] + [women_arrangement]
            total.append(arrangement)
    return total
a = print_arrangements()
for i in a:
    print(i)
print(len(a))



