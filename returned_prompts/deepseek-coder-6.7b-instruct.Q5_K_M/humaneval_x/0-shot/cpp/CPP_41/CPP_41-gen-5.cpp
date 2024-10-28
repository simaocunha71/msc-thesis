    return (n*(n-1))/2; //calculating the number of collisions
}

int main()
{
    int n;
    printf("Enter the number of cars: ");
    scanf("%d",&n);
    printf("The number of collisions is: %d",car_race_collision(n));
    return 0;
}

*/

#include <stdio.h>

int car_race_collision(int n){
    return (n*(n-1))/2; //calculating the number of collisions
}

int main()
{
    int n;
    printf("Enter the number of cars: ");
    scanf("%d",&n);
    printf("The number of collisions is: %d",car_race_collision(n));
    return 0;
}


/*
The logic behind the function is quite simple.

In a car race, if there are n cars moving left and right, then there can be nC2 (combination of 2) collisions between any pair of cars. This is because any car moving left can collide with any car moving right.

For example, if there are 3 cars moving left and 3 cars moving right, the possible collisions are:

1-2, 1-3, 2-3

So, there are 3C2 = 3 pairs of cars that can collide.

In a car race with n cars, there will be nC2 collisions.

So, the function car_race_collision(n) simply calculates the number of pairs of cars that can collide in a car race with n cars.
*/

//Test Case:
//Enter the number of cars: 5
//The number of collisions is: 10
//This is correct because there are 10 pairs of cars that can collide in a car race with 5 cars. They are (5C2) = 10.
//(5*4)/2 = 10

//Enter the number of cars: 10
//The number of collisions is: 45
//This is correct because there are 45 pairs of cars that can collide in a car race with 10 cars. They are