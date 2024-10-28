```
def get_Inv_Count(arr):
    if len(arr) == 1:
        return 0
    else:
        mid = len(arr)//2
        left_count = get_Inv_Count(arr[:mid])
        right_count = get_Inv_Count(arr[mid:])
        inv_count = 0
        left = 0
        right = 0
        merged = []
        while left < mid and right < len(arr):
            if arr[left] <= arr[right]:
                merged.append(arr[left])
                left += 1
            else:
                merged.append(arr[right])
                right += 1
                inv_count += (mid - left)
            if left == mid:
                merged.extend(arr[right:])
                break
            if right == len(arr):
                merged.extend(arr[left:mid])
                break
        return left_count + right_count + inv_count
```
