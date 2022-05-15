# 題目敘述
# 在本題中，我們承接第一題的報童問題，但現在我們不想根據給定的一個存貨量去計算預期利潤；我們想要找出
# 能最大化預期利潤的最佳訂貨量 q*，以及在此訂貨量之下能得到的預期利潤π(q*) 無條件捨去到整數位。
# 以第一題的例子而言，就是 4 跟 18（請自己試著算算看）。如果有數個訂貨量會導致一模一樣的預期利潤
# （是預期利潤一樣，不是無條件捨去之後一樣！），請用比較小的那一個當最佳訂貨量。

import math
c=int(input("enter-"))
r=int(input("enter-"))
N=int(input("enter-"))
lst=list()
for i in range(0,9):
    i=float(input("enter-"))
    lst.append(i)
max_total=0
optimal_q=0
Q=(N*r)//c
for q in range(0,Q+1):
    total=0
    total_1=0
    total_2=0
    n=0
    pro=0
    for n_rate in lst:
        if n != q :
            expect = (n*r-c*q) * n_rate 
            total_1 = total_1 + expect
            n = n+1
            pro = pro + n_rate
        else:
            expect = (n*r-c*q)*(1-pro)
            total_2 = total_2+expect
            break
    total = total_1 +total_2
    # print(total)
    if total > max_total:
        max_total = total
        optimal_q = q
print( optimal_q , math.floor(max_total))