To solve this kata, we should follow these steps:

1. Check if n is greater than m. If true, return -1.
2. Compute the average of the integers from n through m (including n and m).
3. Round the result to the nearest integer.
4. Convert the rounded result to binary.
5. Return the binary result.

Here's a step-by-step breakdown of the solution:

1. We start by checking if n is greater than m. If it is, we return -1, as per the problem's requirements. In the given examples, roundedAvg(7, 5) returns -1, roundedAvg(20, 33) returns "0b11010", and roundedAvg(10, 20) returns "0b1111".

2. If n is not greater than m, we move to the next step. We compute the average of the integers from n through m (including n and m). In the example roundedAvg(1, 5), the average would be (1 + 2 + 3 + 4 + 5) / 5 = 15 / 5 = 3. In the example roundedAvg(10, 20), the average would be (10 + 11 + 12 + 13 + 14 + 15 + 16 + 17 + 18 + 19 + 20) / 11 = 165 / 11 = 14.90909090909091.

3. After computing the average, we round it to the nearest integer. In the example roundedAvg(10, 20), the rounded average is 15 (rounding 14.90909090909091 to the nearest integer).

4. Finally, we convert the rounded result to binary. The binary representation of 15 is 1111, and the binary representation of 14 is 1110.

5. We return the binary result. In the example roundedAvg(1, 5), the binary result is 0b11 (1 in binary). In the example