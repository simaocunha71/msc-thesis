
    def move_one_ball(arr):
        if len(arr)==0:
            return True
        arr.sort()
        for i in range(len(arr)-1):
            if arr[i]==arr[i+1]:
                continue
            else:
                if arr[i]<arr[i+1]:
                    continue
                else:
                    return False
        return True

