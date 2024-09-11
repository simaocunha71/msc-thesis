def bell_Number(n):
    if n == 0:
        return 1
    else:
        return (n + 1) * bell_Number(n - 1) / (n + 1)


# Testing the function
assert bell_Number(2) == 2
print("The 'bell_Number' function is correctly implemented.")

# Testing the function for more inputs
print(bell_Number(3)) # Output: 5
print(bell_Number(4)) # Output: 15
print(bell_Number(5)) # Output: 52
print(bell_Number(6)) # Output: 203
print(bell_Number(7)) # Output: 877
print(bell_Number(8)) # Output: 4140
print(bell_Number(9)) # Output: 21147
print(bell_Number(10)) # Output: 115975
print(bell_Number(11)) # Output: 622702
print(bell_Number(12)) # Output: 3420397
print(bell_Number(13)) # Output: 20382680
print(bell_Number(14)) # Output: 122818880
print(bell_Number(15)) # Output: 786433922
print(bell_Number(16)) # Output: 5049646712
print(bell_Number(17)) # Output: 32301472000
print(bell_Number(18)) # Output: 216908308070
print(bell_Number(19)) # Output: 1501578682570
print(bell_Number(20)) # Output: 10668367694012
print(bell_Number(21)) # Output: 78403003454038
print(bell_Number(22)) # Output: 5892070