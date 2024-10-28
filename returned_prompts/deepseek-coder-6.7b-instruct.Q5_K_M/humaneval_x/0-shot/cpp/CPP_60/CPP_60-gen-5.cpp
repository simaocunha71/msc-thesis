    int sum = 0, i;
    for(i = 1; i <= n; i++)
        sum += i;
    return sum;
}

int main(){
    int n;
    printf("Enter the value of n: ");
    scanf("%d", &n);
    printf("Sum from 1 to %d is: %d\n", n, sum_to_n(n));
    return 0;
}

In this program, we first define a function sum_to_n that takes an integer n as input and returns the sum of numbers from 1 to n. It uses a for loop to calculate the sum.

In the main function, we ask the user to input a number, then we call sum_to_n with this number as the argument and print the returned result.

The complexity of the program is O(n) because of the for loop that runs n times.

Note: The code is written in C++ and the namespace std is used.
*/

/*
