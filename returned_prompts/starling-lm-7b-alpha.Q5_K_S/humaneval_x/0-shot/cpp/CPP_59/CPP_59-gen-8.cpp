    for(int i = 2; i * i <= n; i++){
        while(n % i == 0){
            n /= i;
            goto A;
        }
    }
    return n;
}

int main(){
    int n;
    cin>>n;
    cout<<largest_prime_factor(n);
    return 0;
}

*/

In this program, we need to find the largest prime factor of a number n. Here, we define a function named largest_prime_factor to find the largest prime factor of the number n. The function uses a for loop to iterate through the numbers from 2 to the square root of n. Inside the loop, it checks if n is divisible by i. If it is divisible, it divides n by i and jumps back to the top of the loop using the goto statement. This process continues until n is no longer divisible by i. Finally, the function returns the value of n, which is the largest prime factor of the original number.

In the main function, we take the input value of n and pass it to the largest_prime_factor function. We then print the result using the cout statement.

The code uses the goto statement to jump back to the top of the loop. However, it is important to note that the goto statement is generally not recommended in modern programming practices, as it can make the code difficult to read and maintain.

Overall, the code correctly finds and prints the largest prime factor of the input number.













































































































































































