# 題目敘述
# 有一家電信公司正在研擬一個新服務區域的無線基地臺設置計畫。在這個區域裡，一共有 n 個城鎮，
# 編號為 1、2 直到 n，而城鎮 i 的人口數是 Pi。公司將此區域以一公里為單位，畫出了一個二維座標系，
# 並且以 (x_i, y_i)(xi,yi) 表示城鎮 i 的位置。換句話說，城鎮 i1跟城鎮 i2之間的距離是
# ((xi1 - xi2)^2 + (yi1 - yi2)^2)**(1/2) 
# 公里。如果一個基地臺跟一個城鎮的距離在 d 公里以內，我們就說這個基地臺可以「覆蓋」這個城鎮，
# 也就是這個城鎮的人可以收得到強度足夠的從該基地臺發出的訊號。公司預計在此區域的 n 個城鎮中挑選 p 個
# 城鎮設置基地臺，以求能覆蓋最多的人口數。

# 你在這家電信公司工作，負責挑出這 pp 個城鎮。為此，你設計了一個貪婪演算法。首先在所有城鎮中，
# 你找出「如果蓋在這裡，將可以覆蓋最多人」的城鎮，然後設一個基地臺在那裡。現在你還能再設置 p−1 個
# 基地臺，所以如法泡製，在所有還沒有基地臺的城鎮中，找出「如果蓋在這裡，將可以覆蓋最多還沒被覆蓋的人」
# 的城鎮，設一個基地臺在那裡，然後繼續如此直到挑出 p 個城鎮去設置基地臺為止。如果在任一時刻遇到有
# 兩個以上的城鎮可以被選，就選編號較小的那個。

info=input("n p d :")
n=int(info.split(" ")[0])
p=int(info.split(" ")[1])
d=int(info.split(" ")[2])
# print(n,p,d)

lst_big=list()
lst_big_o=list()
for loc in range(n):
    loc_str= input("x y P:")
    locs=loc_str.split(" ")
    lst_small=list()
    for loc in locs:
        lst_small.append(int(loc))
    lst_big.append(lst_small)
    lst_big_o.append(lst_small)
# print(lst_big)

#演算法
target_plc=-1
total_optimal_target_plc=list()
total_optimal_population=0
for one_plc in range(p):
    lst_population=list()
    lst_population_elements=list()
    for plc in lst_big:
        max_population=0
        max_population_elements=list()
        other_plcs=list()
        # lst_population_num_small=list()

        for i in lst_big:
            other_plcs.append(i)
        other_plcs.remove(plc)
        for other_plc in other_plcs:
            dis = ((plc[0] - other_plc[0]) **2 + (plc[1] - other_plc[1])**2)**(1/2)
            if dis <= d:
                # print(other_plc)
                max_population = max_population + other_plc[2]
                max_population_elements.append(lst_big.index(other_plc)+1)
                # print(max_population)
        lst_population.append((lst_big.index(plc) + 1, max_population + plc[2]))
        lst_population_elements.append(max_population_elements)
    # print(lst_population)
    # print(lst_population_elements)

    optimal_population=0 
    for optimal_population_number in lst_population:
        if optimal_population_number[1] > optimal_population:
            optimal_population = optimal_population_number[1]
            target_plc = optimal_population_number[0]

    remove_lst_big=list()
    optimal_target_plc = lst_big_o.index(lst_big[target_plc-1])+1
    total_optimal_target_plc.append(optimal_target_plc)
    total_optimal_population = total_optimal_population + optimal_population

    for element in lst_population_elements[target_plc-1]:
        remove_lst_big.append(lst_big[element-1])
    remove_lst_big.append(lst_big[target_plc-1])
    for element in remove_lst_big:
        lst_big.remove(element)
    
    # print(lst_big)
    # print(target_plc, optimal_population)
print(total_optimal_target_plc, total_optimal_population)
    

        
            

                  
        


        