    if b == 0:
        return a
    else:
        return GreatestCommonDivisor(b, a % b)

}
# test the function
print(GreatestCommonDivisor(3, 5))  # 1
print(GreatestCommonDivisor(25, 15))  # 5

