# 題目敘述
# 你經營一家報攤專賣一份日報，今天下午你得在報社關門前下訂單，告訴報社你要為明天訂購幾份報紙，
# 隔天清晨你就會收到訂購的報紙並且付款。每份報紙的進貨價格是 c 元，賣給客人的零售價則是 r 元。
# 每天會來多少個客人想買報紙是件不確定的事，也就是說單日需求量 D 是隨機的。根據過往經驗，你估計明天
# 的單日需求量會落在 0 和 N 之間，並且符合如下的機率分佈：

# Pr(D=i)=pi，i=0,1,...,N。
# 其中min{q,D} 是明天的銷售量（訂貨量和需求量中比較小的那個數字）、E[min{q,D}] 是預期銷售量
# （也就是銷售量取期望值）、rE[min{q,D}] 是預期銷售收益、cqcq 則是必須付給報社的進貨成本。
# 這是一個作業管理（operations management）領域的經典存貨問題（inventory problem），因為是很多存
# 貨管理方法的基礎，被特別給予一個名稱叫「報童問題」（newsvendor problem）。


import math
c=int(input("enter-"))
r=int(input("enter-"))
n=int(input("enter-"))
q=int(input("enter-"))
total_1=0
total_2=0
pro=0
for n in range(0,n+1):
    n_rate=float(input("enter-"))
    if q != n:
        expect=(n*r-c*q)*n_rate 
        # print(expect)
        total_1 = total_1 + expect   
    else:
        expect=(n*r-c*q)*(1-pro)
        total_2 = total_2 + expect
        # print(expect)
        break
    pro= pro+ n_rate
    # print(expect)
total=total_1+total_2
print(math.floor(total))
