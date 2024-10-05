    int collision = 0;
    for(int i=0; i<n; i++){
        for(int j=0; j<n; j++){
            collision +=1;
        }
    }
    return collision;
}

int main(){
    int n;
    scanf("%d", &n);
    printf("%d", car_race_collision(n));
    return 0;
}

// The code is a simple representation of the problem and it is assuming that n cars are moving left to right and n cars are moving right to left. 
// The function car_race_collision is calculating the total number of collisions between n cars moving left to right and n cars moving right to left. 
// It is assumed that the number of cars are equal, i.e., n cars are moving left to right and n cars are moving right to left. 
// So, in total there will be n*n number of collisions.
// The main function is taking the input number of cars and printing the total number of collisions.


// Time complexity: O(n^2)
// Space complexity: O(1)

// Test Cases:
// Input: 3
// Output: 9
// Explanation: 3 cars are moving left to right and 3 cars are moving right to left. Total number of collisions will be 3*3 = 9.

// Input: 4
// Output: 16
// Explanation: 4 cars are moving left to right and 4 cars are moving right to left. Total number of collisions will be 4*4 = 16.

// Input: 5
// Output: 25
// Explanation: 5 cars are moving left to right and 5 cars are moving right to left. Total number of collisions will be 5*5 = 25.


/*
Note: The code is assuming that n cars are moving left to right and n cars are moving right to left. 
So, in total there will be n*n number of collisions.
*/

// Time complexity: O(n^2)
// Space complexity: O(1)

// Test Cases:
// Input: 3
// Output: 9
// Explanation