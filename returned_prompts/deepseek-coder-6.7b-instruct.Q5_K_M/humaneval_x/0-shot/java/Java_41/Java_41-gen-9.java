        int totalCollisions = 0;

        // Each car in the left moving group will collide with each car in the right moving group.
        // Hence, the total number of collisions will be the product of the number of cars in each group.
        totalCollisions = n * n;

        return totalCollisions;
    }

}

Here I used the formula to calculate the total number of collisions which is the product of the number of cars in each moving group.


This is the correct answer, but the question asked for a solution that works for an infinite line. As the line is infinite, we can't actually calculate the exact number of collisions. But we can say that the number of collisions will be approximately equal to the number of cars in each group.

*/

