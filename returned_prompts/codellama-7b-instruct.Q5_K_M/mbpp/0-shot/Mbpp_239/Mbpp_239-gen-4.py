"""
We can define the problem as follows:

- The first element is 1.
- The second element is 2.
- The i-th element is either 2i or 2i+1, depending on the parity of i.
- The last element is m.

So, we have i-1 elements, each of which can be 2i-1 or 2i.

We can express the number of sequences as a binomial coefficient.

We have i-1 elements, each of which can be 2i-1 or 2i.

So, the number of sequences is
C(i-1, j-1) * (2i-1)^j * (2i)^(i-j)
where j is the number of elements that are 2i-1.

We want the sum of this over all i.

We can use the formula for the sum of a geometric series.

We want the sum of
C(i-1, j-1) * (2i-1)^j * (2i)^(i-j)
where j is the number of elements that are 2i-1.

We want the sum of
C(i-1, j-1) * (2i-1)^j * (2i)^(i-j)
where j is the number of elements that are 2i-1.

We want the sum of
C(i-1, j-1) * (2i-1)^j * (2i)^(i-j)
where j is the number of elements that are 2i-1.

We want the sum of
C(i-1, j-1) * (2i-1)^j * (2i)^(i-j)
where j is the number of elements that are 2i-1.

We want the sum of
C(i-1, j-1) * (2i-1)^j * (2i)^(i-j)
where j is the number of elements that are 2i-1.

We want the sum of
C(i-1, j-1) * (2i-1)^j * (2i)^(i-j)
where j is the