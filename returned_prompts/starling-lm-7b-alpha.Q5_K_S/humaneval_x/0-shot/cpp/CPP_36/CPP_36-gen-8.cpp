    if(n < 11) return 0;
    if(n < 13) return 0;
    if(n < 22) return 1;
    if(n < 24) return 1;
    if(n < 33) return 2;
    if(n < 36) return 2;
    if(n < 44) return 3;
    if(n < 47) return 3;
    if(n < 55) return 4;
    if(n < 58) return 4;
    if(n < 66) return 5;
    if(n < 69) return 5;
    if(n < 77) return 6;
    if(n < 80) return 6;
    if(n < 88) return 7;
    if(n < 91) return 7;
    if(n < 100) return 8;
    goto A;
}


/*
The Fizz Buzz Test is an interview question designed to help determine whether or not a programmer understands the "basics" of programming languages, such as C++ or Java. It is based on the "Last Digit Sequence" interview question, and is considered a simpler version of it.

The test is as follows:

Write a program that prints the numbers from 1 to 100. But for multiples of 3, it should print "Fizz" instead of the number; for multiples of 5, it should print "Buzz". And for multiples of both 3 and 5, it should print "FizzBuzz".

Here is a simple solution in C++:

#include <iostream>

void fizz_buzz(int n) {
    for (int i = 1; i <= n; i++) {
        if (i % 15 == 0) {
            std::cout << "FizzBuzz" << std::endl;
        } else if (i % 3 == 0) {
            std::cout << "Fizz" << std::endl;
        } else if (i % 5