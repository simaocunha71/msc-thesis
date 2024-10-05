    vector<int> factors;
    for(int i = 2; i <= n; i++){
        while(n % i == 0){
            factors.push_back(i);
            n /= i;
        }
    }
    return factors;
}

int main(){
    int num;
    printf("Enter a number: ");
    scanf("%d", &num);
    vector<int> factors = factorize(num);
    printf("Prime factors are: ");
    for(int i = 0; i < factors.size(); i++)
        printf("%d ", factors[i]);
    return 0;
}

/*
Output:
Enter a number: 70
Prime factors are: 2 5 7 
*/

The C++ code takes an integer input from the user and uses the function 'factorize' to find all the prime factors of that number.
The function factorize takes an integer input and iterates from 2 to that number.
For each iteration, it checks if the current number is a factor of the input number.
If it is, it adds that number to the vector 'factors' and divides the input number by that number.
It continues this process until the input number becomes 1.
Finally, it returns the vector 'factors'.
The main function prints the prime factors of the input number.
*/

The complexity of this code is O(n), as it goes through each number from 2 to n once.

Please note that the above solution works well for smaller numbers but for very large numbers, the algorithm will take a lot of time.
*/

//This is a C++ solution for the problem of finding prime factors.
//It uses a simple iterative approach to find the factors.
//The time complexity of this solution is O(n).
//The space complexity is also O(n) because we are storing the factors in a vector.
//The vector can grow in size up to n, so the space complexity is linear.
//If you want a more efficient solution, you would need to use a more complex algorithm.
//For example, you could use the Sieve of Eratosthenes to find all prime numbers up to n, then divide n by each prime number.
//This would be