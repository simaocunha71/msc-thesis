"""
def extract_singly(nums):
    new_list = []
    for i in nums:
        for j in i:
            new_list.append(j)
    return new_list

def extract_singly(nums):
    return [item for sublist in nums for item in sublist]
"""

def extract_singly(nums):
    return [item for sublist in nums for item in sublist]

def extract_singly(nums):
    return set(item for sublist in nums for item in sublist)


"""
def extract_singly(nums):
    return {item for sublist in nums for item in sublist}
"""

# set({3, 4, 5})
# set({4, 5, 7, 1})

"""
def extract_singly(nums):
    return sum(map(lambda x: set(x), nums), set())
"""

# def extract_singly(nums):
#     return reduce(lambda x,y: x.union(y), nums, set())

# def extract_singly(nums):
#     return functools.reduce(lambda x,y: x.union(y), nums, set())

# def extract_singly(nums):
#     return operator.reduce(lambda x,y: x.union(y), nums)

# def extract_singly(nums):
#     return operator.reduce(lambda x,y: x.union(y), nums)

# def extract_singly(nums):
#     return reduce(lambda x,y: x.union(y), nums)

# def extract_singly(nums):
#     return reduce(set.union, nums)

# def extract_singly(nums):
#     return reduce(set.update, nums)

# def extract_singly(nums):
#     return reduce(set, nums)

# def extract_singly(nums):
#     return reduce(set.add, nums)

# def extract_singly(nums