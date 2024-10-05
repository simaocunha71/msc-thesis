    # Your solution here
    def order_by_points(nums):
        nums = sorted(nums, key = lambda x: (sum(map(int, str(x))), x))
        return nums

    return nums





# Made By Mostafa_Khaled
```
    
        
        
```

```