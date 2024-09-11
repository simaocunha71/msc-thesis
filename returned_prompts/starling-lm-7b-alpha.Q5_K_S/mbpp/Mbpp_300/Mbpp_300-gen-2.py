Here's a step-by-step guide to solving this problem:

1. First, note that the sum of the first n bits and the sum of the last n bits will always be equal to 2^n, since each bit has a 50% chance of being set and a 50% chance of not being set.

2. Next, recognize that you can break the problem down into finding all binary sequences of length n such that the sum of the first half of the bits is less than or equal to 2^(n/2), and the sum of the second half of the bits is less than or equal to 2^(n/2). This is because if the sum of the first half is greater than 2^(n/2), then there are not enough 1s in the second half to make the sums equal.

3. To find all binary sequences of length n such that the sum of the first half of the bits is less than or equal to 2^(n/2), you can use a recursive approach. Start with an empty sequence and add a 1 to the front of the sequence. Then, calculate the sum of the first half of the bits and check if it is less than or equal to 2^(n/2). If it is, add the sequence to a list of valid sequences. Then, repeat this process with the same sequence but with a 0 added to the front. Continue this process until you have generated all valid sequences.

4. Once you have found all binary sequences of length n such that the sum of the first half of the bits is less than or equal to 2^(n/2), you can use a similar recursive approach to find all binary sequences of length n such that the sum of the second half of the bits is less than or equal to 2^(n/2). This will involve starting with an empty sequence and adding a 1 to the front, calculating the sum of the second half of the bits, and checking if it is less than or equal to 2^(n/2). If it is, add the sequence to a list of valid sequences. Repeat this process until you have generated all valid sequences.

5. Finally, return the total count of valid sequences from both recursive approaches. This will give you the count of all binary sequences of length 2n such that the sum