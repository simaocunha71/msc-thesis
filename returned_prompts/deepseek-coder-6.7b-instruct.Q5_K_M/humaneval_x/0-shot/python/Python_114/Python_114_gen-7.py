
    # 우선 배열을 오름차순으로 정렬합니다.
    nums.sort()

    # 가장 작은 합은 배열의 첫 번째 요소 또는 두 개의 요소의 합으로 구성될 수 있습니다.
    min_sum = nums[0] + nums[1]

    # 배열을 순회하면서 가장 작은 합을 구합니다.
    for i in range(2, len(nums)):
        min_sum = min(min_sum, nums[i])

    return min_sum

print(minSubArraySum([2, 3, 4, 1, 2, 4]))  # 1
print(minSubArraySum([-1, -2, -3]))  # -6


# 이 코드는 배열을 정렬하고 첫 번째 및 두 번째 요소의 합을 기본적으로 가장 작은 합으로 설정합니다.
# 그런 다음 배열을 순회