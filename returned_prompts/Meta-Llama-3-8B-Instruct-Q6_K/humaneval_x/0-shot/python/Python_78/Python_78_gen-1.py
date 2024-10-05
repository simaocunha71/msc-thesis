    def hex_key(num):
        count = 0
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
        hex_dict = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
        for i in num:
            if i.isdigit():
                for j in range(2, int(i) + 1):
                    if int(i) % j == 0:
                        break
                else:
                    count += 1
            elif i.upper() in hex_dict:
                if hex_dict[i.upper()] in primes:
                    count += 1
        return count
    print(hex_key("AB")) # 1
    print(hex_key("1077E")) # 2
    print(hex_key("ABED1A33")) # 4
    print(hex_key("123456789ABCDEF0")) # 6
    print(hex_key("2020")) # 2
    print(hex_key("1A")) # 1
    print(hex_key("11")) # 1
    print(hex_key("101")) # 1
    print(hex_key("F")) # 1
    print(hex_key("E")) # 0
    print(hex_key("D")) # 1
    print(hex_key("C")) # 0
    print(hex_key("B")) # 1
    print(hex_key("A")) # 1
    print(hex_key("0")) # 0
    print(hex_key("1")) # 1
    print(hex_key("2")) # 1
    print(hex_key("3")) # 1
    print(hex_key("4")) # 0
    print(hex_key("5")) # 1
    print(hex_key("6")) # 0
    print(hex_key("7")) # 1
    print(hex_key("8")) # 0
    print(hex_key("9")) # 0
    print(hex_key("")) # 0
    print(hex_key("ABC")) # 2
    print(hex_key("123")) # 2
    print(hex_key("123456789")) # 2
    print(hex_key("ABCDEF")) # 2
   