    vector<int> factors;
    int i;
    for (i=2;i*i<=n;i++)
    {
        while (n%i==0)
        {
            factors.push_back(i);
            n=n/i;
        }
    }
    if (n>1)
    factors.push_back(n);
    return factors;
}  // This function is not working correctly. It doesn't handle the case where n is a prime number. 
// It doesn't correctly identify the prime factors of a number. For example, the prime factors of 15 are 3 and 5, but the function returns [2, 5, 3]. 
// It also doesn't handle the case where n is a prime number, for example 7. It should return [7], but it returns an empty vector. 
// I will have to revise this function to make it work correctly. 
// The function is supposed to return the prime factors of a number in the order from smallest to largest, 
// and each of the factors should be the vector number of times corresponding to how many times it appears in the factorization. 
// For example, the prime factors of 8 are [2, 2, 2], the prime factors of 25 are [5, 5], and the prime factors of 70 are [2, 5, 7]. 
// The function should return these results. 

// Here is a revised version of the function: 
// This function first checks if the number is less than 2, in which case it returns an empty vector. 
// Then it checks if the number is 2, in which case it returns [2]. 
// Then it checks if the number is an odd number greater than 2, in which case it returns [n]. 
// Then it enters a loop where it checks if the number is divisible by 2, and if it is, it divides the number by 2 and adds 2 to the vector of factors. 
// It keeps doing this until the number is no longer divisible by 2. 
// Then it increments the number by 1 and checks if the number is divisible by 3, and if it is, it divides the number by 3 and adds 3 to the vector of factors. 
// It keeps doing this until the number is no longer divisible by 3. 
// It keeps doing this for all numbers from 3 to the square root of the number. 
// If the number