/* The code above doesn't work.  The code below works, but is not very efficient.
Can you write a much more efficient code than the code below?
*/

    int n1=n,n2=n;
    while(n1>0){
        while(n2>0){
            n1--;
            n2--;
        }
        n2=n;
        n--;
    }
    return n;

B:
/*
I have a working solution for this problem that runs in O(n) time.
I think the solution is cool, so I'm sharing it here.  It's not very intuitive.

Here's the idea:

1. We assume all cars have unique speeds.  Since we don't know the speeds of the
cars, we assume that the speeds of the cars are randomly distributed between 0 and 1.
2. We define the variable p.  For a pair of cars, we assume that p is the probability
that the two cars collide.  The value of p is a number between 0 and 1.
3. We assume that p is the same for all pairs of cars.  We can prove this by induction:
    * For a pair of cars, we can assume that p is the same for all pairs of cars.
    * Now, consider a group of n cars.  We can assume that p is the same for all pairs
      of cars in the group.
    * Now, consider a group of n+1 cars.  We can assume that p is the same for all pairs
      of cars in the group.
4. We can calculate p using the following formula:
    * The probability that a car collides with a car to its left is 1/n.
    * The probability that a car collides with a car to its right is 1/n.
    * The probability that a car collides with a car to its left or right is 1/(n-1).
    * Therefore, p = 1/n + 1/n - 1/(n-1) = 2/n - 1/(n-1).
    * Since p is a number between 0 and 1, we can assume that p is the same for all pairs
      of cars.
5. We can calculate the expected number of collisions using the following formula:
    * The expected number of collisions is p * n * (n-1) / 2.
6. We can use the following formula to calculate the expected number of collisions:
   