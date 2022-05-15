# 題目敘述
# 你經營一家報攤專賣一份日報，今天下午你得在報社關門前下訂單，告訴報社你要為明天訂購幾份報紙，
# 隔天清晨你就會收到訂購的報紙並且付款。每份報紙的進貨價格是 c 元，賣給客人的零售價則是 r 元，
# 而每一份沒賣出去的報紙，在明天結束時可以被以一份 s 元的殘值（salvage value）當作廢紙賣掉。
# 每天會來多少個客人想買報紙是件不確定的事，也就是說單日需求量 D 是隨機的。根據過往經驗，
# 你估計明天的單日需求量會落在 0 和 N 之間，並且符合如下的機率分佈：

#Pr(D=i)=pi，i=0,1,...,N。

import math
c=int(input("enter-"))
r=int(input("enter-"))
N=int(input("enter-"))
S=int(input("enter-"))
lst=list()
for i in range(0,N+1):
    i=float(input("enter-"))
    lst.append(i)
max_total=0
optimal_q=0
Q=((N*r)-(N*S))// -(S-c)
# print(Q)
for q in range(0,Q+1):
    total=0
    total_1=0
    total_2=0
    n=0 # 從需求量為0時開始試
    pro=0
    for n_rate in lst:
        if n != q :
            expect = (n*r - c*q + (q-n)*S) * n_rate 
            total_1 = total_1 + expect
            n = n+1
            pro = pro + n_rate
        else:
            expect = (n*r - c*q + (q-n)*S)*(1-pro)
            total_2 = total_2+expect
            break
    total = total_1 +total_2
    # print(total)
    if total > max_total:
        max_total = total
        optimal_q = q
print( optimal_q , math.floor(max_total))