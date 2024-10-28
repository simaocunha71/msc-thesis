def swap_List(list):
    size = len(list)
  
    # Swapping 
    temp = list[0]
    list[0] = list[size - 1]
    list[size - 1] = temp
  
    return list