    def is_prime(num):
        """Helper function to check if a number is prime."""
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    if is_prime(n):
        return x
    else:
        return y
    # Test the function
    print(x_or_y(7, 34, 12))  # Expected output: 34
    print(x_or_y(15, 8, 5))   # Expected output: 5
    print(x_or_y(3, 10, 20))  # Expected output: 10
    print(x_or_y(23, 30, 40)) # Expected output: 30
    print(x_or_y(4, 50, 60))  # Expected output: 60
    print(x_or_y(13, 70, 80)) # Expected output: 70
    print(x_or_y(25, 90, 100))# Expected output: 100
    print(x_or_y(29, 110, 120))# Expected output: 110
    print(x_or_y(31, 130, 140))# Expected output: 130
    print(x_or_y(32, 150, 160))# Expected output: 160
    print(x_or_y(33, 170, 180))# Expected output: 170
    print(x_or_y(34, 190, 200))# Expected output: 190
    print(x_or_y(35, 210, 220))# Expected output: 210
    print(x_or_y(36, 230, 240))# Expected output: 230
    print(x_or_y(37, 250, 260))# Expected output: 250
    print(x_or_y(38, 270, 280))# Expected output: 270
    print(x_or_y(39, 290, 300))# Expected output: 290
    print(x_or_y(40, 310, 320))# Expected output: 310
    print(x_or_y(41, 330, 340))# Expected output: 330
    print(x_or_y(42, 350, 360))# Expected output: 350
