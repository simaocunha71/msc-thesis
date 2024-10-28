    vector<int> primes;
    int i;
    if(n<2)
    return primes;
    primes.push_back(2);
    for (i=3;i<n;i+=2)
    {
        bool is_prime=true;
        for (int j=3;j<=sqrt(i);j+=2)
        {
            if (i%j==0)
            {
                is_prime=false;
                break;
            }
        }
        if (is_prime)
        primes.push_back(i);
    }
    return primes;
}
```

I have provided the solutions to the given problems in C++. The first problem "Check if in given vector of numbers, are any two numbers closer to each other than given threshold" checks if there are any two numbers in the vector that are closer than a given threshold. The second problem "Separate groups of nested parentheses into separate strings" separates the groups of nested parentheses in a string into separate strings. The third problem "Truncate a number into its decimal part" truncates a number into its decimal part. The fourth problem "Count up to n prime numbers" counts up to a given number n the first n prime numbers.

In each problem, the solution is provided in a C++ function. The function takes the necessary parameters and returns the desired result. The problems are solved using various C++ features such as vectors, loops, conditional statements, and mathematical functions.

The first problem uses a nested loop to check for pairs of numbers that are closer than the given threshold. The second problem uses a loop to iterate through the string and a counter to keep track of the level of nesting. The third problem uses the modulo operator to check if a number is an integer and the subtraction operator to calculate the decimal part. The fourth problem uses a loop to iterate through the numbers and a conditional statement to check if a number is prime.