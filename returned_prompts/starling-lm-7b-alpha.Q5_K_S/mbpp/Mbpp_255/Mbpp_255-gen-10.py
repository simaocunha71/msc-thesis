def top_k(nums, k):
    return sorted(nums, reverse=True)[:k]

# assert top_k([3,1,4,2],2)==[4,3,2,1]
# print