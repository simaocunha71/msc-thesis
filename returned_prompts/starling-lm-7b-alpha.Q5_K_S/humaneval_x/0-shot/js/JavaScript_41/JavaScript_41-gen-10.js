To solve this problem we can use the formula for the sum of an arithmetic series, which is:

sum = (n * (first + last)) / 2

In this case, we have n cars moving to the right, each with a speed of n, and n cars moving to the left, each with a speed of n. The first car moving to the left will collide with the first car moving to the right after a time of:

t = (n * n) / (n + n) = n

After this time, all the cars will have moved n units to the right, so the first car moving to the left will collide with the (n + 1)th car moving to the right. This pattern continues, with each car moving to the right colliding with the (i + 1)th car moving to the left, where i is the index of the car moving to the right.

To find the total number of collisions, we can sum the number of collisions for each car moving to the right. The number of collisions for the i-th car moving to the right is i. So, the total number of collisions is the sum of the first n natural numbers, which is (n * (n + 1)) / 2.

The function `carRaceCollision` calculates this sum and returns the result.

Here's an example of how to use the function:

```javascript
console.log(carRaceCollision(3)); // Output: 3
```

In this example, there are 3 cars moving to the right and 3 cars moving to the left. The first car moving to the right collides with the second car moving to the left, the second car moving to the right collides with the third car moving to the left, and the third car moving to the right collides with the fourth car moving to the left. The total number of collisions is 3.

This problem can be solved using the formula for the sum of an arithmetic series, as the pattern of collisions follows an arithmetic sequence. By calculating the sum of the first n natural numbers, we can determine the total number of collisions in the car race.

Note: It's important to note that the cars in this problem are assumed to be infinitely sturdy and strong