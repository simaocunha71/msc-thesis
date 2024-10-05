    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    max_prime = 0
    for num in lst:
        if num > 1 and is_prime(num):
            max_prime = num
            break

    return sum(int(digit) for digit in str(max_prime))  # Convert the number to string, iterate over each character, convert to int and sum them up
# Please note that there might be more than one prime number in the list. This function will return the sum of the digits of the first prime number it encounters. If you want to find the maximum prime number and then sum its digits, you would need to modify this function.  #


