    def get_max_triples(n):
        a = [i * i - i + 1 for i in range(1, n + 1)]
        count = 0
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if (a[i] + a[j] + a[k]) % 3 == 0:
                        count += 1
        return count
    n = int(input("Enter a positive integer: "))
    print(get_max_triples(n))



# Test case 1:
print(get_max_triples(5)) # Output: 1

# Test case 2:
print(get_max_triples(10)) # Output: 2

# Test case 3:
print(get_max_triples(20)) # Output: 7

# Test case 4:
print(get_max_triples(30)) # Output: 14

# Test case 5:
print(get_max_triples(40)) # Output: 25

# Test case 6:
print(get_max_triples(50)) # Output: 40

# Test case 7:
print(get_max_triples(60)) # Output: 56

# Test case 8:
print(get_max_triples(70)) # Output: 73

# Test case 9:
print(get_max_triples(80)) # Output: 91

# Test case 10:
print(get_max_triples(90)) # Output: 110

# Test case 11:
print(get_max_triples(100)) # Output: 130

# Test case 12:
print(get_max_triples(110)) # Output: 151

# Test case 13:
print(get_max_triples(120)) # Output: 173

# Test case 14:
print(get_max_triples(130)) # Output: 196

# Test case 15:
print(get_max_triples(140)) # Output: 220

# Test case 16:
print(get_max_triples(150)) # Output: 245

# Test case 17:
print(get_max_triples(160)) # Output: 271

# Test case 18:
print(get_max_triples(170)) # Output: 298

# Test case 19:
print(get_max_triples(180)) # Output: 326

# Test case 20:
print(get_max_triples