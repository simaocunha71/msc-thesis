
def div_list(nums1: list, nums2: list) -> list:
    if len(nums1) != len(nums2):
        raise ValueError("The lengths of the input lists must be equal")
    return [num1/num2 for num1,num2 in zip(nums1,nums2)]


