    for (int i=2; i<100; i++)
    for (int j=i; j<100; j++)
    for (int k=j; k<100; k++)
    {
        if (i*j*k==a)
        {
            if (is_prime(i) && is_prime(j) && is_prime(k))
            return true;
        }
    }
    return false;
}

bool is_prime(int a)
{
    if(a<=1) return false;
    for(int i=2; i*i<=a; i++)
        if(a%i==0) return false;
    return true;
} 
// is_prime function is a helper function that checks whether a number is prime or not. It returns true if the number is prime and false otherwise. It does this by checking if the number is divisible by any number up to its square root. If it is divisible, it is not prime. If it is not divisible by any of these numbers, it is prime. 
// The is_multiply_prime function works by checking all possible combinations of three numbers between 2 and 100. If the product of these three numbers equals the given number, it checks if each of these numbers is prime using the is_prime function. If they are all prime, it returns true. If it doesn't find any such combination, it returns false. 
// Note that this function is not very efficient, as it checks all possible combinations of three numbers. There are more efficient ways to solve this problem, such as using a prime number sieve to generate all prime numbers up to 100, and then checking if the given number is the product of three of these prime numbers. 
// Also, the is_prime function could be optimized by only checking divisibility up to the square root of the number, as mentioned in the comment. 
// This solution is correct but not efficient. A more efficient solution would be to generate all prime numbers up to 100 and then check if the given number can be represented as the product of three of these prime numbers. 
// The time complexity of this solution is O(n^3), where n is the maximum number that can be a prime number. The space complexity is O(n), for storing the prime numbers. 
// A more efficient solution would be to generate all prime numbers up to 100 and then check if the given number can be represented as the product of three of these prime numbers. This would reduce the time complexity to O(n) and the space complexity to O(n).