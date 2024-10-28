def check_Consecutive(List):
    List.sort()
    for i in range(len(List)-1):
        if List[i+1]-List[i] != 1:
            return False
    return True