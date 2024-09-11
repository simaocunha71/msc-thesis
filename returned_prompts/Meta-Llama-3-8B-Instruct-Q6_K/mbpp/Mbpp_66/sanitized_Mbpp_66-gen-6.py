def pos_count(lst):
    return sum(1 for num in lst if num > 0)  # or use len([num for num in lst if num > 0]) if you prefer list comprehension
    # or even more concise: return sum(1 for num in lst if num > 0) if you prefer generator expression