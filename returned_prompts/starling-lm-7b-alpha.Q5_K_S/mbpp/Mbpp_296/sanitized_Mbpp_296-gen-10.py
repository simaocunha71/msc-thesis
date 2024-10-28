def get_Inv_Count(input_arr):
    count = 0
    for i in range(len(input_arr)):
        for j in range(i+1,len(input_arr)):
            if(input_arr[i]>input_arr[j]):
                count+=1
    return count