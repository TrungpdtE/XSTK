import random

## CÂU 1
n = int(input('Nhập vào số lần thí nghiệm: '))
print();
print(f'Số lần thí nghiệm là {n}')
print();
print('CÂU 1:')
#tạo xúc xắc
def roll_dice():
    return random.randint(1, 6)

#tung 2 viên xúc xắc
def experiment():
    dice1 = roll_dice()
    dice2 = roll_dice()
    return dice1, dice2

#số lần thí nghiệm là n
#nhập vào n từ bàn phím

#Xác xuất tung 2 viên giống nhau
def XS2VienGiongNhau(n):
    Count= 0

    for _ in range(n):
        dice1, dice2= experiment()
        if dice1== dice2:
            Count+= 1

    XS = Count/n
    return XS

XS = XS2VienGiongNhau(n)
print(f'Xác xuất tung được 2 viên giống nhau : {XS}')

#Xác xuất hai viên khác nhau
def XS2VienKhacNhau(n):
    Count = 0
    for _ in range(n):
        dice1, dice2= experiment()
        if dice1!= dice2:
            Count+= 1
    XS = Count/n
    return XS
print(f'Xác xuất tung được 2 viên khác nhau: {XS2VienKhacNhau(n)}')
#Xác xuất cả viên cùng số chẵn
def XS2VienCungChan(n):
    Count= 0

    for _ in range(n):
        dice1, dice2= experiment()
        if dice1 % 2 == 0 and dice2 % 2 == 0:
            Count+= 1

    XS = Count/n
    return XS
print(f'Xác xuất tung được 2 viên cùng chẵn: {XS2VienCungChan(n)}')

#Xác xuất tung 2 viên cùng lẻ
def XS2VienCungLe(n):
    Count = 0

    for _ in range(n):
        dice1, dice2= experiment()
        if dice1 % 2!= 0 and dice2% 2!= 0:
            Count+= 1

    XS = Count/n
    return XS
print(f'Xác xuất tung 2 viên cùng lẻ: {XS2VienCungLe(n)}')
#Xác xuất 2 viên không đồng lẻ, đồng chẵn
def XS1Le1Chan(n):
    Count= 0
    for _ in range(n):
        dice1, dice2= experiment()
        if (dice1%2== 0 and dice2%2!= 0) or (dice1%2!= 0 and dice2%2== 0):
            Count+=1
    XS = Count/n
    return XS
print(f'Xác xuất 2 viên không đồng lẻ, đồng chẵn: {XS1Le1Chan(n)}')
#Xác xuất cả 2 đều là 6
def XS2so6(n):
    Count= 0
    for _ in range(n):
        dice1, dice2= experiment()
        if dice1== 6 and dice2== 6:
            Count+= 1
    XS = Count/n
    return XS
print(f'Xác xuất cả 2 đều là 6: {XS2so6(n)}')
#Xác xuất cả 2 là tổng lớn hơn 10
def XSTong2VienHon10(n):
    Count= 0
    for _ in range(n):
        dice1, dice2= experiment()
        if dice1+dice2> 10:
            Count+=1
    XS = Count / n
    return XS
print(f'Xác xuất cả 2 là tổng lớn hơn 10: {XSTong2VienHon10(n)}')


## CÂU 2
print();
print('CÂU 2:')
#Bốc 3 viên từ bình, có 3 màu 2xanh, 3đỏ, 5trắng
def Boc3vien():
    Vien = ['xanh', 'xanh', 'đỏ', 'đỏ', 'đỏ', 'trắng', 'trắng', 'trắng', 'trắng', 'trắng']
    baVien = random.sample(Vien, 3)
    return baVien
#Cả ba viên cùng màu
def XSCungMau(n):
    Count= 0
    for _ in range(n):
        baVien= Boc3vien()
        if baVien.count(baVien[0])== 3:
            Count+= 1
    XS= Count/n
    return XS
print(f'Xác xuất cả ba viên cùng màu: {XSCungMau(n)}')

#Cả ba viên đều khác màu nhau
def XSKhacNhau(n):
    Count= 0
    for _ in range(n):
        baVien= Boc3vien()
        if len(set(baVien))== 3:
            Count+= 1

    XS= Count/n
    return XS
print(f'Xác xuất cả ba viên đều khác màu nhau: {XSKhacNhau(n)}')

# Chỉ có hai viên cùng màu
def XS2Cungmau(n):
    Count= 0
    for _ in range(n):
        baVien= Boc3vien()
        Counts= [baVien.count(vien) for vien in set(baVien)]
        if 2 in Counts:
            Count+= 1
    XS= Count/n
    return XS
print(f'Xác xuất chỉ có hai viên cùng màu: {XS2Cungmau(n)}')

#Được 2 bi đỏ và 1 bi trắng
def XS2Do1Trang(n):
    Count = 0

    for _ in range(n):
        baVien = Boc3vien()
        if baVien.count('đỏ') == 2 and baVien.count('trắng') == 1:
            Count += 1
    probability_two_red_one_white = Count / n
    return probability_two_red_one_white

#Liệt kê các trường hợp 3 bi đều màu trắng.
def XS3Trang(n):
    Count= 0

    for _ in range(n):
        baVien= Boc3vien()
        if baVien.count('trắng')== 3:
            Count+= 1

    XS= Count/n
    return XS
print(f'Xác xuất 3 viên đều màu trắng: {XS3Trang(n)}')  

#Liệt kê các trường hợp 3 bi đều màu trắng.
def LK3Trang(n):
    TH = []
    for _ in range(n):
        baVien = Boc3vien()
        if baVien.count('trắng') == 3:
            TH.append(baVien)
    return TH

print('Liệt kê các trường hợp 3 bi đều màu trắng:')
print(LK3Trang(n))

print();
#Bai 3
print('Bai 3:')
#Bóc 4 lá
def bocBai():
    suits= ['hearts', 'diamonds', 'clubs', 'spades']
    ranks= ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    deck= [(suit, rank) for suit in suits for rank in ranks]
    bonLa= random.sample(deck, 4)
    return bonLa

#Bốn lá cùng chất
def XScungChat(n):
    Count = 0
    for _ in range(n):
        bonLa = bocBai()
        if len(set(card[0] for card in bonLa))== 1:
            Count+= 1
    XS= Count/n
    return XS
print(f'Xác xuất bốn lá cùng chất: {XScungChat(n)}')

#Bốn lá đôi một khác chất
def XSdoikhachat(n):
    Count= 0
    for _ in range(n):
        bonLa= bocBai()
        if len(set(card[0] for card in bonLa))== 4:
            Count+= 1
    XS= Count/n
    return XS
print(f'Xác xuất bốn lá đôi một khác chất: {XSdoikhachat(n)}')

#Bốn lá cùng màu
def XScungMau(n):
    Count= 0
    for _ in range(n):
        bonLa= bocBai()
        colors = [card[0] in ['hearts', 'diamonds'] for card in bonLa]
        if colors.count(colors[0])== 4:
            Count+= 1
    XS= Count/n
    return XS
print(f'Xác xuất bốn lá cùng màu: {XScungMau(n)}')

# Bốn lá cùng chỉ số (tứ quý)
def XStuQuy(n):
    Count= 0
    for _ in range(n):
        bonLa= bocBai()
        if len(set(card[1] for card in bonLa)) == 1:
            Count+= 1
    XS= Count/n
    return XS
print(f'Xác xuất bốn lá cùng chỉ số (tứ quý): {XStuQuy(n)}')

#Bốn lá cùng là loại số
def XScungSo(n):
    Count= 0
    for _ in range(n):
        bonLa= bocBai()
        if all(card[1].isdigit() for card in bonLa):
            Count+= 1
    XS= Count/n
    return XS
print(f'Xác xuất bốn lá cùng là loại số: {XScungSo(n)}')

#Bốn lá cùng loại hình
def XScungChat(n):
    Count= 0
    for _ in range(n):
        bonLa= bocBai()
        if all(card[1] in ['J', 'Q', 'K', 'A'] for card in bonLa):
            Count += 1
    XS= Count/n
    return XS
print(f'Xác xuất bốn lá cùng loại hình: {XScungChat(n)}')

#Cau 4
print();
import itertools
print('Cau 4:')
#Tạo một tập hợp để lưu các quả banh. Ký hiệu 2 quả banh màu trắng là 'W1', 'W2'. Tương tự cho 3 quả xanh dương là 'B1', 'B2', 'B3' và 4 quả màu đỏ là 'R1', 'R2', 'R3'. 'R4'. Lưu vào biến URN.
URN = {'W1', 'W2', 'B1', 'B2', 'B3', 'R1', 'R2', 'R3', 'R4'}
print('a')
print(URN)
#Tìm tập con gồm 3 quả banh từ tập hợp URN trên (không phân biệt thứ tự). Lưu kết quả của tập con đó vào biến U3.
U3 = list(itertools.combinations(URN, 3))
print('b')
print(U3)
#Liệt kê các trường hợp 3 quả banh được chọn ở câu (b) có một quả banh màu trắng, một quả banh màu xanh dương và một quả banh màu đỏ, kết quả lưu vào biến white1blue1red1.
LKTrang_Duong_Do = []
for Banh in U3:
    Trang = False
    Xanh = False
    Do = False
    for banh in Banh:
        #trang
        if 'W' in banh:
            Trang = True
        #do
        if 'B' in banh:
            Xanh = True
        #xanh
        if 'R' in banh:
            Do = True
    if Trang and Xanh and Do:
        LKTrang_Duong_Do.append(Banh)
print('c')
print(LKTrang_Duong_Do)
#Tính xác suất chọn ngẫu nhiên 3 quả banh trong đó có một quả banh màu trắng, một quả banh màu xanh dương và một quả banh màu đỏ, kết quả lưu vào biến P.
P= len(LKTrang_Duong_Do)/len(U3)
print('d')
print(P)

print();
#Cau 5
print('Cau 5:')
# Tạo bộ bài
chat = ['co', 'ro', 'bich', 'tep']
so = list(range(1, 14))  # 1-10, J=11, Q=12, K=13

#Taọ bộ bài
bo_bai = []
for c in chat:
    for s in so:
        bo_bai.append((c, s))

#Bốc 5 lá
def BOcBai():
    return random.sample(bo_bai, 5)

#Kiểm tra có phải sảnh ko
def Sanh(baiRut):
    baiRut = sorted(baiRut, key=lambda x: x[1])
    for i in range(4):
        if baiRut[i][1] != baiRut[i+1][1] - 1:
            return False
    return True

#xác xuất thực nghiệm
def XSTN(n):
    Count = 0
    for _ in range(n):
        if Sanh(BOcBai()):
            Count += 1
    return Count / n
#Xác xuất lí thuyết
#C(52, 5) = 2598960 cách để chọn 5 lá, 40 sảnh có thể có
def XSLT():
    return 40 / 2598960
print("Xác suất lý thuyết: ", XSLT())
print("Xác suất thực nghiệm: ", XSTN(10000))

print();
#Cau 6
# print('Cau 6:')
E = {0, 1, 2, 3, 4, 5}
LK3chuSo = []
for i in range(1, 6):  
    for j in E:
        for k in E:
            LK3chuSo.append(str(i) + str(j) + str(k))
print("Liệt kê các số có 3 chữ số: ")
print(LK3chuSo)

# Liệt kê các số có 4 chữ số (đôi một khác nhau) từ tập hợp E
LK4chuSo = []
for i in range(1, 6):
    for j in E:
        if j != i:
            for k in E:
                if k != i and k != j:
                    for l in E:
                        if l != i and l != j and l != k:
                            LK4chuSo.append(str(i) + str(j) + str(k) + str(l))
print("Liệt kê các số có 4 chữ số: ")
print(LK4chuSo)