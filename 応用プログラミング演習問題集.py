# 第1章
# 1-1
print ('Hello World')
print(4+4*5)

# 1-2
print('''11211
12121
21112''')

# 第2章
# 例題2-1
print('(33+44)*55=', (33+44)*55)
print('2.1+4.3+6.5=', 2.1+4.3+6.5)
print('(123+456)%78=', (123+456)%78)

# 例題2-2
x = 123*45
print(x)

# 例題2-3
x = 9.99
y = 50
print(x*10, y*10)

# 例題2-4
x = 10
y = 10
print(x,y)  # 10,10が出る

x = y+10
y = 20
print(x,y)  # 20,20が出る

x = x-10
y = y-x
print(x,y)  # 10,10が出る

# 2-1
print(1+2+3+4+5)
print(1*3*5*7*9)
print(98*3+48*4+188+(208-50)*5)

# 2-2
#(1) andやnot:予約語、　1文字目が数字
#(2) 省略
#(3) 省略

# 2-3
#(1) 省略
#(2) 10,0 になるはず

# 2-4
x = 10*20
y = 30*40
print(x,y)

# 2-5
x = 1.5
print(x / 10)

# 2-6
x = 10
print(x)
x = 20
print(x)
x = 30
print(x)

# 第3章
# 3-1 (1)
x = int(input('整数を入れてください'))
print(x)

# 3-1 (2)(3)はとばす
# 3-1 (4)
x = int(input('seisuu = ?'))
print(x)

# 3-1 (5)
x = float(input('小数を入れてください'))
print(x)

# 3-2 (1)
print('整数を2回入れてください。和が出ます。')
x = int(input())
y = int(input())
print(x+y)

# 3-2 (2)
print('整数を3回入れてください。和が出ます。')
x = int(input())
y = int(input())
z = int(input())
print(x+y+z)

# 3-2 (3)
print('小数を2回入れてください。和が出ます。')
x = float(input())
y = float(input())
print(x+y)

# 3-2 (4)
print('整数を2回入れてください。積が出ます。')
x = int(input())
y = int(input())
print(x*y)

# 3-3 -1
shakkin = int(input('借金額を入力してください'))
hensai = int(input('月の返済額を入力してください'))
year = (shakkin / hensai)//12
month = (shakkin / hensai) % 12
print('返済にかかる年月は', year, '年', month, 'ヶ月です。')

# 3-3 -2
bonus = int(input('毎年のボーナスから返済したい額を入力してください'))
year2 = ((shakkin-bonus)/hensai)/12
print('ボーナスから', bonus, '円返済すると、', year-year2, '年返済が早まります。')

# 3-3 -3
nensu = int(input('返済を完了したい年数を入力してください。'))
bonus2 = shakkin - (nensu * hensai)
print(nensu, '年で返済を完了するにはボーナスで', bonus2, '円返済してください')

# 3-4  改行して変数を表示する方法が他にないか聞きたい
print('整数を2回、小数を2回入力してください。表示します')
x = int(input())
y = int(input())
w = float(input())
z = float(input())
print(x)
print(y)
print(z)
print(w)

# 3-5
print('整数を4回入力してください。和を表示します')
x = int(input())
y = int(input())
z = int(input())
w = int(input())
print(x+y+z+w)

# 3-6
print('はじめに整数を2回入力してください。積を表示します')
x = int(input())
y = int(input())
print('seki=',x*y)
print('次に、さらに整数を2回入力してください。積を表示します')
z = int(input())
w = int(input())
print('seki=',z*w)
print('goukei=',x*y+z*w)

# 3-7
print('整数を2回入力してください。和差積を表示します')
x = int(input())
y = int(input())
print('和は',x+y)
print('差は',abs(x-y))
print('積は',x*y)

# 第4章
# 例題4-1
if 0<10:
    print ('OK')

# 例題4-2:
x = int(input('値を入れてください。ある数字と等しいか判定します'))
if x+25000 == 3500*9:
    print('OK')
else:
    print('Booo')

# 例題4-3
x = int(input('値を入れてください'))
if x > 0:
    print('positive')
    if x > 100:
        print('100ijou')
    else:
        print('100miman')
elif x == 0:
    print('zero')
else:
    print('negative')

# 4-1 (1)
x = int(input('値を入れてください'))
if x == 0:
    print('zero')

# 4-1 (2)
x = int(input('値を入れてください'))
if x >= 100:
    print('OK')

# 4-1 (3)
x = int(input('値を入れてください'))
if x > 0:
    print('positive')
else:
    print('negative')

# 4-1 (4)
x = int(input('値を入れてください'))
y = int(input('値を入れてください'))
if x == y:
    print('equal')

# 4-2 (1)
x = int(input('値を入れてください'))
if x == 10:
    print('x=10')
elif x > 10:
    print('x>10')
else:
    print('x<10')

# 4-2 (2)
x = int(input('値を入れてください'))
if x == 1:
    print('x=1')
elif x == 2:
    print('x=2')
else:
    print('etc')

# 4-2 (3)
x = int(input('値を入れてください'))
if x < 0:
    if x == 0:
        print('zero')
    else:
        print('negative')
elif x > 0:
    print('positive')
    if x >= 100:
        print('100ijou')
    else:
        print('100miman')

# 4-3
print('値を2つ入力してください。')
x = int(input('一つ目'))
y = int(input('二つ目'))
if x >= y:
    print(x-y)
else:
    print('マイナスになります')

# 4-4
x = int(input('1~3の値を入れてください'))
if x == 1:
    print('(。-∀-)')
elif x == 2:
    print('( *´艸｀)')
else:
    print('(*^^)v')

# 4-5
x = int(input('整数を入力してください'))
if x % 2 == 0:
    print('Guusuu')
else:
    print('Kisuu')

# 4-6
x = int(input('値を入れてください'))
if 10 <= x <= 20:
    print('ok')

# 4-7
x = int(input('値を入れてください'))
if 10 <= x <= 20:
    print('(^_-)-☆')
elif 50 <= x <= 60:
    print('(/・ω・)/')

# 4-8
x = int(input('値を入れてください'))
if x > 0:
    print(x)
else:
    y = int(input('値を入れてください'))
    print(x*y)

# 第5章
# 5-1(1)
num = 0
while num < 2:
    x = int(input("値を入れてください"))
    print(x)
    num = num + 1
    continue

# 5-1(2)
num = 0
while num < 2:
    x = int(input("なにか値を入れてください"))
    y = int(input("もうひとつ値を入れてください"))
    print(x,y)
    num = num + 1
    continue


# 5-1(3)
num = 0
while num < 2:
    x = int(input("価格を入れてください"))
    x = x * 1.08
    print("税込み価格は", x,"円です")
    num = num + 1
    continue

# 5-1 (4) --(1)について直した
while True:
    x = int(input("値を入れてください。0で終わります"))
    if x == 0:
        break
    else:
        print(x)
        continue

# 5-1 (5) --(1)について直した
while True:
    x = int(input("値を入れてください。負の数ならで終わります"))
    if x < 0:
        break
    else:
        print(x)
        continue

# 5-2 (1)
while True:
    x = int(input("値を入れてください。0なら終わります"))
    if x == 0:
        break
    elif x%7 == 0:
        print(x,"は7の倍数です")
        continue
    else:
        print(x, "は7の倍数ではありません")
        continue

# 5-2 (2) は7を3にすればいいだけだから省略

# 5-2 (3)
while True:
    x = int(input("値を入れてください。0なら終わります"))
    if x == 0:
        break
    elif x < 0:
        print(x,"は負の数です")
        continue
    else:
        print(x, "は負の数ではありません")
        continue

# 5-3(1)
i = 1
while i<=10:
    print("Hello!")
    i = i+1

# 5-3(2)
i = 1
while i<=20:
    print("Hello!!")
    i = i+1

# 5-4(1)
x = 1
while x<=10:
    print(x)
    x = x+1

# 5-4(2) は10を20にするだけ
# 5-4(3)
x = -10
while x<=10:
    print(x)
    x = x+1

# 5-4(4)
x = 1
while x <= 10:
    if x%2 == 0:
        print(x)
    x = x+1

# 5-4(5) --(1)であれば9この表示になる。

# 5-5(1)
for i in range(1,11):
    print(i)

for i in range(1,21):
    print(i)

for i in range(-10,11):
    print(i)

for i in range(1,11):
    if i%2 == 0:
        print(i)

# 5-5(2)
for i in range(10,0,-1):
    print(i)

# 5-5(3)
for i in range(1,102):
    if i%2 == 0:
        print(i)

# 5-6(1) --リストにしてみたけど合ってるのか
y = []
for i in range(10):
    x = int(input("値を入れてください"))
    if x == 0:
        break
    y.append(x)
print(y)

# 5-6(2) はrangeを20にするだけ
# 5-6(3) はif x==10: にするだけ
# 5-6(4) はif x<0 :　にするだけ
# 5-6(5) はif x=0 or x=1にするだけ

# 5-6(6)
for i in range(10):
    x = int(input("値を入れてください"))
    if x == 0:
        break
    else:
        print(x)
        continue

# 5-7(1) --枠線なし
for i in range(1,10):
    for j in range(1,10):
        print(i*j, end=" ")
    print(" ") 

# 5-7(1) --枠線ありも作れた
for i in range(1,10):
    for j in range(1,10):
        if i*j <10:
            print(i*j, end=" |")
        else:
            print(i*j, end="|")
    print(" ") 
    for z in range(1,10):
        print("――", end="―")
    print(" ")

# 5-7(2)
for i in range(0,10):
    for j in range(0,10):
        if i+j <10:
            print(i+j, end=" |")
        else:
            print(i+j, end="|")
    print(" ") 
    for z in range(0,10):
        print("――", end="―")
    print(" ")

# 5-7(3)
for i in range(1,12):
    for j in range(1,12):
        if i*j <10:
            print(i*j, end="  |")
        elif i*j < 100:
            print(i*j, end=" |")
        else:
            print(i*j, end="|")
    print(" ") 
    for z in range(1,12):
        print("――", end="――")
    print(" ")

# 5-8
n=1
for i in range(5,0,-1):
    print(" "*n, end="")
    print("#"*i*2)
    n = n+1

# 5-9 --whileにする必要ってなんだろう
while True:
    x1 = int(input("値を入れてください"))
    x2 = int(input("値を入れてください"))
    if x1 == x2:
        break
    print("(。-∀-)")
    break

# 5-10
import random
while True:
    x = random.randint(1,100)
    print(x)
    if x == 50:
        break

# 5-11
import random
x = random.randint(1,100)
while True:
    y = int(input("値を入れてください。数当てゲームです"))
    if x == y:
        print("当たり！")
        break
    elif x > y:
        print("この値よりも大きい値です")
    else:
        print("この値よりも小さい値です")

# 5-12 (1)
x = int(input("値を入れてください"))
y = int(input("それより大きい値を入れてください"))
for i in range(x,y+1):
    print(i)

# 5-12 (2)
a = int(input("値を入れてください"))
b = int(input("それより大きい値を入れてください"))
while a<=b:
    print(a)
    a = a+1

# 5-13 (1)
a = int(input("値を入れてください"))
b = int(input("値を入れてください"))
for i in range(a):
    print("*"*b)

# 5-13 (2)
a = int(input("値を入れてください"))
b = int(input("値を入れてください"))
for i in range(a):
    for j in range(b):
        print("*", end="")
    print(" ")

# 5-14 --横線は長すぎたため省略、縦線のみ。
for i in range(1,10):
    for j in range(1,10):
        if i*j <10:
            print(i,"×",j,"=",i*j, end=" |")
        else:
            print(i,"×",j,"=",i*j, end="|")
    print(" ") 

# 5-15
for i in range(1,4):
    for j in range(1,4):
        for w in range(1,4):
            if i*j*w < 10:
                print(i,"×",j,"×",w,"=",i*j*w, end=" |")
            else:
                print(i,"×",j,"×",w,"=",i*j*w, end="|")
    print(" ") 


# 5-16
while True:
    x = int(input("値を入れてください。0で終了します"))
    if x == 0:
        break
    else:
        print(x)
        print("#"*x)

# 5-17
for n in range(2,101):
    for i in range(2,n):
        if n%i == 0:
            break
    else:
        print(n)
    n = n+1

# 第6章
# 例題6-1
y = input("x= ")
x = input("x= ")
while y != x :
    y = x
    x = input("x= ")

# 例題6-2
m = -9999
for i in range(10):
    j = int(input("Please enter an integer:"))
    if m < j :
        m = j
print(m)

# 例題6-3
c = 0
for i in range(10) :
    j = int(input("Please enter an integer:"))
    if j > 10:
        c += 1
print(c)

# 例題6-4
f = 0
for i in range(10):
    j = int(input("Please enter an integer:"))
    if j == 5:
        f = 1
if f ==1:
    print("5はあった")

# 6-1 (1)
n = 100000
while True:
    x = int(input("値を入れてください"))
    if n*2 < x:
        break
    else:
        n=x

# 6-1 (2)
y = int(input("値を入れてください"))
x = int(input("値を入れてください"))
while y!=x:
    if x<0:
        y=x
    x = int(input("値を入れてください"))

# 6-1 (3)
z = input("x =")
y = input("x =")
x = input("x =")
while z != x:
    z = y
    y = x
    x = int(input("x ="))

# 6-2 (1)
m = 10000
for i in range(10):
    i = int(input("値を入れてください"))
    if m>i :
        m = i
print(m)

# 6-2 (2)
m = 0
for i in range(5):
    x = int(input("値を入れてください"))
    if x<=10 and m<x:
        m=x
print("10以下で最大の値は",m,"でした")

# 6-3 (1)
c = 0
for i in range(10):
    x = int(input("値を入れてください"))
    if x<0 :
        c += 1
print(c,"回負の数が入力されました")

# 6-3 (2)
c = 0
for i in range(10):
    x = int(input("値を入れてください"))
    if x%2 == 0:
        c += 1
print(c,"回偶数が入力されました。")

# 6-4 (1)
f = 0
for i in range(10):
    x = int(input("値を入れてください"))
    if x == 5:
        f = 1
if f == 0:
    print("5がありません")

# 6-4 (2)
f = 0
for i in range(10):
    x = int(input("値を入れてください"))
    if x<0 :
        f = 1
if f == 1:
    print("負の数がありました")
else:
    print("負の数はありませんでした")

# 6-5
y = 0
for i in range(10):
    x = int(input("値を入れてください"))
    y += x
print(y)

# 6-6 --リスト型にしたけど合ってるのかな
y = []
z = 0
while True:
    x = int(input("値を入れてください"))
    if x == 0:
        y.append(0)
        print(y)
        break
    else:
        z += x
        y.append(x)
        y.append(z)

# 6-7
c0 = 0
c1 = 0
for i in range(10):
    x = int(input("値を入れてください"))
    if x == 0 :
        c0 += 1
    elif x == 1 :
        c1 += 1
if c0 > c1:
    print("0の方が1より多く入力されました")
elif c0 < c1:
    print("1の方が0より多く入力されました")

# 6-8
f = 0
x = int(input("素数判定です。値を入れてください"))
for i in range(2,x):
    if x%i == 0:
        f = 1
if f == 1:
    print(x,"は素数ではありません")
else:
    print(x,"は素数です")

# 6-9
n = int(input("素数判定です。値を入れてください"))
for j in range(2,n):
    f = 0
    for i in range(2,j):
        if j%i == 0:
            f = 1
    if f == 0:
        print(j)

# 6-10
import random
c = 0
for i in range(100):
    x = random.randint(1,100)
    if x <= 30:
        c += 1
print("乱数で30以下の数字が",c,"回入力されました")

# 6-11
c = 0
y = int(input("値を入れてください"))
for i in range(10):
    x = int(input("値を入れてください"))
    if x == y :
        c += 1
    y = x
print(c,"回連続して前回と同じ数が入力されました")