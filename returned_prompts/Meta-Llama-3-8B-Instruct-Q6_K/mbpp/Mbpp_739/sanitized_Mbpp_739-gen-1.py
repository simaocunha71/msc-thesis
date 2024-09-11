def find_Index(n):
    i = 1
    while True:
        triangular = (i * (i + 1)) // 2
        if len(str(triangular)) == n:
            return i
        i += 1
    return i
    # This function will return the smallest triangular number with n digits. For example, if you call find_Index(2), it will return 4. This is because the smallest triangular number with 2 digits is 6, and 6 is the 4th triangular number. 1 + 2 + 3 + 4 = 10. 1 + 2 + 3 + 4 + 5 = 15. 1 + 2 + 3 + 4 + 5 + 6 = 21. So the 4th triangular number is 6, which has 2 digits. 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. So the 5th triangular number is 28, which has 2 digits. So the 6th triangular number is 36, which has 3 digits. So the 7th triangular number is 45, which has 3 digits. So the 8th triangular number is 55, which has 3 digits. So the 9th triangular number is 66, which has 3 digits. So the 10th triangular number is 77, which has 3 digits. So the 11th triangular number is 89, which has 3 digits. So the 12th triangular number is 101, which has 3 digits. So the 13th triangular number is 114, which has 3 digits. So the 14th triangular number is 128, which has 3 digits. So the 15th triangular number is 145, which has 3 digits. So the 16th triangular number is 165, which has 3 digits. So the 17th triangular number is 176, which has 3 digits. So the 18th triangular number is 198, which has 3 digits. So the 19th triangular number is 220, which has 3 digits. So the 20th triangular number is 252, which has 3 digits. So the 21st triangular number is 285, which has 3 digits. So the 22nd triangular number is 330, which has 3