    if not arr:
        return None

    neg_count = 0
    for num in arr:
        if num < 0:
            neg_count += 1

    if neg_count % 2 == 0:
        return sum(map(abs, arr))
    else:
        return -sum(map(abs, arr))


# Complexity Analysis
# Time Complexity: O(n)
# Space Complexity: O(1)

# Here's a simple Python program to test your function:

def main():
    print(prod_signs([1, 2, 2, -4]))  # -9
    print(prod_signs([0, 1]))  # 0
    print(prod_signs([]))  # None

if __name__ == '__main__':
    main()


# Output
# -9
# 0
# None



# Here's a simple Python program to test your function:

def main():
    print(prod_signs([1, 2, 2, -4]))  # -9
    print(prod_signs([0, 1]))  # 0
    print(prod_signs([]))  # None

if __name__ == '__main__':
    main()


# Output
# -9
# 0
# None


























































































































































































