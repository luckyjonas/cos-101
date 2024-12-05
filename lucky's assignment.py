num_list =[1,2,3,4,5,6,6,7,8,9,10]

list2 = num_list.copy

list3 =[]

for _ in num_list:
    list3.append(list2[-1])
    list2.pop(-1)

    num_list = list3
    print(num_list)
