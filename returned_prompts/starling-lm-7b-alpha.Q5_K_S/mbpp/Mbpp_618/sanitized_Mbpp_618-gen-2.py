def div_list(list1,list2):
    list3=[]
    for i in range(len(list1)):
        list3.append(list1[i]/list2[i])
    return list3
list1 = list(map(int,input("Enter first list: ").strip().split()))
list2 = list(map(int,input("Enter second list: ").strip().split()))