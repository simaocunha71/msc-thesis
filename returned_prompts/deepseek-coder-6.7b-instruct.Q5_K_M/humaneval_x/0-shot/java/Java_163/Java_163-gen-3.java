
def get_odd_collatz(n):
    def collatz(n):
        if n == 1:
            return [1]
        else:
            if n % 2 == 0:
                return [n] + collatz(n // 2)
            else:
                return [n] + collatz(3 * n + 1)

    collatz_sequence = collatz(n)
    odd_numbers = [num for num in collatz_sequence if num % 2 != 0]
    return sorted(odd_numbers)

print(get_odd_collatz(5))  # returns [1, 5]

The collatz function recursively generates the collatz sequence for a given number. Then, using a list comprehension, we filter out all the even numbers from the collatz sequence and return the resulting list sorted in increasing order.
</details>

## 2. Binary Search

<details>
<summary>