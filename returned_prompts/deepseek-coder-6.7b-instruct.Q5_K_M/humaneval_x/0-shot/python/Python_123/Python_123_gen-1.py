
    def collatz(n):
        seq = [n]
        while n != 1:
            if n % 2 == 0:
                n = n // 2
            else:
                n = 3 * n + 1
            seq.append(n)
        return seq

    def get_odd_collatz(n):
        return sorted(set(i for i in collatz(n) if i % 2 != 0))

print(get_odd_collatz(5))

# Output:
# [1, 5]

Explanation: 

In the Collatz sequence for n=5, the odd numbers are 1, 5, 16, 8, 4, 2. As we only need the odd numbers, we filter them out using the condition i % 2 != 0, and then sort the remaining numbers in increasing order.


