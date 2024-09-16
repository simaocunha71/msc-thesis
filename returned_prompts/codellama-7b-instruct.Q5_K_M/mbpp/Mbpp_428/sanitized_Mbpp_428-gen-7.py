def shell_sort(arr):
    # 分组
    group = len(arr) // 2
    while group > 0:
        # 每个组内排序
        for i in range(group, len(arr)):
            j = i
            while j >= group and arr[j] < arr[j-group]:
                arr[j], arr[j-group] = arr[j-group], arr[j]
                j -= group
        # 分组缩小一半
        group = group // 2
    return arr