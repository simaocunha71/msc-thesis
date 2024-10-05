const seq = [3];
  if (n === 0) return [];
  for (let i = 1; i <= n; i++) {
    if (i % 2 === 0) {
      seq.push(1 + i / 2);
    } else {
      seq.push(seq[i - 1] + seq[i - 2] + seq[i + 1]);
    }
  }
  return seq;
};

























/*Fibonacci sequence is a sequence of numbers in which each number after the first two is the sum of the two preceding. The Fibonacci sequence starts with 0 and 1:

Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

The Fibonacci sequence is a famous sequence in mathematics, and it is a powerful tool to understand and analyze certain types of patterns and relationships. It is used in various fields, including computer science, finance, and art.

The Fibonacci sequence is defined by the recurrence relation:

F(n) = F(n−1) + F(n−2)

with seed values:

F(1) = 1
F(2) = 1

Here's a Python function that calculates the Fibonacci sequence up to a given number:

def fibonacci(n):
    if n == 0:
        return []
    fib = [0, 1]
    while len(fib) < n + 1:
        fib.append(fib[-1] + fib[-2])
    return fib[:n + 1]

You can use this function to get the first 10 Fibonacci numbers:

print(fibonacci(10)) # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

The time complexity of this function is O(n) because it requires n iterations to generate the Fibon