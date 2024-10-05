        int totalCollisions = 0;
        for(int i=0; i<n; i++){
            totalCollisions += i;
        }
        return totalCollisions;
    }
}

This code calculates the number of collisions based on the assumption that each car moving left to right will collide with 'i' number of cars moving right to left. This is because if a car moving left to right is the 'i'th car, then it will collide with all the cars before it moving right to left. Thus, the total number of collisions is the sum of all integers from 0 to n-1, which is (n*(n-1))/2.

Test cases:

Input: 3
Output: 3
Explanation: The cars are numbered 0, 1, 2. Car 0 collides with cars 0, 1, 2. Car 1 collides with cars 0, 1, 2. Car 2 collides with car 0.

Input: 1
Output: 0
Explanation: There are no collisions as there is only one car.

Input: 5
Output: 10
Explanation: The cars are numbered 0, 1, 2, 3, 4. Car 0 collides with cars 0, 1, 2, 3, 4. Car 1 collides with cars 0, 1, 2, 3. Car 2 collides with cars 0, 1, 2. Car 3 collides with car 0. Car 4 collides with car 0.

*/

// This code is contributed by Anshuman Goyal

// This code is contributed by Anshuman Goyal

// This code is contributed by Anshuman Goyal

// This code is contributed by Anshuman Goyal

// This code is contributed by Anshuman Goyal

// This code is contributed by Anshuman Goyal

// This code is contributed by Anshuman Goyal

// This code is contributed by Anshuman Goyal

// This code is contributed by Anshuman Goyal

// This code is contributed by Anshuman Goyal
