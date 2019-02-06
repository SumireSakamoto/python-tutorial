# 第7章
# 7-1
def sub(n):
    print("#"*n)

# 7-2 --本当は\nで区切りたいが、先頭に変なスペースが出てくるため断念
def sub1(l,m,n):
    print("#"*l)
    print("#"*m)
    print("#"*n)

# 7-3
def sub2(n):
    print("#"*n)

for i in range(1,7):
    sub2(i)

# 7-4
def seihu(a):
    if a>0:
        print(1)
    elif a<0:
        print("?1")
    else:
        print(0)

# 7-5 -1
def goukei(a):
    b=int(input("値を入れてください"))
    print(a+b)

# 7-5 -2 はいまいちよく分からない。（都度合計が出てしまわない？）

# 第8章は無かった

# 第9章
# 例題9-1
a=[i*10 for i in range(100)]
print(a)

# 9-1
a=[]
for i in range(10):
    x = int(input("値を入れてください"))
    a.append(x)
a.reverse()

print(a)

# 9-2
import random
x=[0,0,0,0]
for i in range(100):
    r = random.randint(0,3)
    x[r] += 1

print(x)

# 9-3
def sub3(l,m,n,o):
    print("#"*l)
    print("#"*m)
    print("#"*n)
    print("#"*o)

import random
x=[0,0,0,0]
for i in range(100):
    r = random.randint(0,3)
    x[r] += 1

sub3(*x)

# 9-4
a=[0,0,0,0,0,0,0,0,0,0]
for i in range(10):
    x=int(input("値を入れてください"))
    x = x//10
    a[x] += 1
print(a)

# 9-5
a=[0,0,0,0,0,0,0,0,0,0]
a1=int(input("値を入れてください"))
a2=int(input("値を入れてください"))
for i in range(a1,a2):
    a[i] += 1
print(a)

# 9-6
def nine6(n,i):
    n[i] += 1

# 9-7 --聞かれている意味がいまいち。。 そういう関数があるのだろうか？

# 追加問題1
L=["Taro","Jiro","Saburo","Shiro","Goro"]

# 追加問題2
print(L[0])
print(L[-1])

# 追加問題3
print(len(L))

# 追加問題4
range(10,100,3)

# 追加問題5
range(100,10,-2)

# 追加問題6
height=[165,180,155,170,171]
print(sorted(height))

# 追加問題7
height=[165,180,155,170,171]
print(sorted(height))
