"""
def get_pairs_count(nums, sum):
    pairs = []
    for i,num in enumerate(nums):
        for j,num_j in enumerate(nums):
            if i!=j and num + num_j == sum:
                pairs.append(sum)
    return len(pairs)

# Testing
assert get_pairs_count([1