"""
The number of possible sequences is given by the following recurrence relation:
C(m, n) = C(m-1, n-1) + C(m-2, n-1) + ... + C(m-n, n-1)

where C(m, n) is the number of possible sequences of length n, such that each element is a positive integer and is greater than or equal to twice the previous element but less than or equal to m.

Let's try to prove it by induction:

Base case:
C(m, 1) = 1
C(m, 2) = 2

Inductive step:
Let C(m, n) be the number of possible sequences of length n, such that each element is a positive integer and is greater than or equal to twice the previous element but less than or equal to m.

Let C(m-1, n-1) be the number of possible sequences of length n-1, such that each element is a positive integer and is greater than or equal to twice the previous element but less than or equal to m-1.

Then, the number of possible sequences of length n, such that each element is a positive integer and is greater than or equal to twice the previous element but less than or equal to m, is:
C(m, n) = C(m-1, n-1) + C(m-2, n-1) + ... + C(m-n, n-1)

Let's prove that C(m, n) = C(m-1, n-1) + C(m-2, n-1) + ... + C(m-n, n-1) is true.

Let's consider the following sequence:
1 2 3 4 5 ... n

We can make it a valid sequence of length n, such that each element is a positive integer and is greater than or equal to twice the previous element but less than or equal to m, by adding the following elements:

1 2 3 4 5 ... n-1

Let's prove that the above sequence is a valid sequence of length n-1, such that each element is a positive integer and is greater than or equal to twice the previous element but less than or equal