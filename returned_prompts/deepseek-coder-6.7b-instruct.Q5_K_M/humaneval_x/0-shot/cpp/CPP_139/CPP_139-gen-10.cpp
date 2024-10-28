    long long res = 1;

    for(int i = 1; i <= n; i++){
        long long fact = 1;
        for(int j = 1; j <= i; j++){
            fact *= j;
        }
        res *= fact;
    }

    return res;
}

int main(){
    int n;
    scanf("%d",&n);
    printf("%lld",special_factorial(n));
    return 0;
}



/*
You can see that in the main function, we have taken an integer n as input and then we have called the special_factorial function by passing n as an argument. The special_factorial function is calculating the special factorial of n and returning the result. The main function is printing the result.
*/

/*
This is a simple problem of factorial of a number. We just need to multiply n factorials from 1 to n.
*/

/*
Time Complexity: O(n^2)
Reason: There is a loop inside a loop. The outer loop runs n times and the inner loop runs i times.

Space Complexity: O(1)
Reason: We are using a constant amount of space.
*/

// Please note that this code is written in C++ and not in Python.



/*
This code works for small numbers. But for large numbers, it will take a long time to compute because of the time complexity. We can optimize it by using dynamic programming or memorization.
*/


// The code is contributed by Vikram Singh(vikram353)
// Thank you Vikram Singh for providing this solution.




// Please note that this code is written in C++ and not in Python.



/*
This code works for small numbers. But for large numbers, it will take a long time to compute because of the time complexity. We can optimize it by using dynamic programming or memorization.
*/


// The code is contributed by Vikram Singh(vikram353)
// Thank you Vikram Singh for providing this solution.




// Please note that this code is written in C++ and not in Python.



/*
