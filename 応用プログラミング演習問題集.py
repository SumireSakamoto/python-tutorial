# 第1章
# 1-1
print ('Hello World')
print(4+4*5)

# 1-2
print('''11211
12121
21112''')

# 第2章
# 例2-1
print('(33+44)*55=', (33+44)*55)
print('2.1+4.3+6.5=', 2.1+4.3+6.5)
print('(123+456)%78=', (123+456)%78)

# 例2-2
x = 123*45
print(x)

# 例2-3
x = 9.99
y = 50
print(x*10, y*10)

# 例2-4
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
# 3-1(1)
x = int(input('整数を入れてください'))
print(x)

# 3-1(2)(3)はとばす
# 3-1(4)
x = int(input('seisuu = ?'))
print(x)

# 3-1(5)
x = float(input('小数を入れてください'))
print(x)

# 3-2(1)
print('整数を2回入れてください。和が出ます。')
x = int(input())
y = int(input())
print(x+y)

# 3-2(2)
print('整数を3回入れてください。和が出ます。')
x = int(input())
y = int(input())
z = int(input())
print(x+y+z)

# 3-2(3)
print('小数を2回入れてください。和が出ます。')
x = float(input())
y = float(input())
print(x+y)

# 3-2(4)
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
# 例4-1
if 0<10:
    print 'OK'

# 例4-2:
x = input('値を入れてください。ある数字と等しいか判定します')
if x+25000 == 3500*9:
    print('OK')
else:
    print('Booo')

# 例4-3
x = input('値を入れてください')
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
x = input('値を入れてください')
if x == 0:
    print('zero')

# 4-1 (2)
x = input('値を入れてください')
if x >= 100:
    print('OK')

# 4-1 (3)
x = input('値を入れてください')
if x > 0:
    print('positive')
else:
    print('negative')

# 4-1 (4)
x = input('値を入れてください')
y = input('値を入れてください')
if x == y:
    print('equal')

# 4-2 (1)
x = input('値を入れてください')
if x == 10:
    print('x=10')
elif x > 10:
    print('x>10')
else:
    print('x<10')

# 4-2 (2)
x = input('値を入れてください')
if x == 1:
    print('x=1')
elif x == 2:
    print('x=2')
else:
    print('etc')

# 4-2 (3)
x = input('値を入れてください')
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
x = input('一つ目')
y = input('二つ目')
if x >= y:
    print(x-y)
else:
    print('マイナスになります')

# 4-4
x = input('1~3の値を入れてください')
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
x = input('値を入れてください')
if 10 <= x <= 20:
    print('ok')

# 4-7
x = input('値を入れてください')
if 10 <= x <= 20:
    print('(^_-)-☆')
elif 50 <= x <= 60:
    print('(/・ω・)/')

# 4-8
x = input('値を入れてください')
if x > 0:
    print(x)
else:
    y = input('値を入れてください')
    print(x*y)

