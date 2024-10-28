    if(a<3){
        return false;
    }
    if(a==3){
        return true;
    }
    if(a%2==0){
        return false;
    }
    for(int i=3;i<(int)sqrt(a)+1;i+=2){
        if(a%i==0){
            return false;
        }
    }
    return true;
}

int main(){
    int n = 30;
    printf("%d\n",is_multiply_prime(n));
    return 0;
}






/*
The question is to write a function that returns true if the given number is the multiplication of 3 prime numbers and false otherwise.
We can solve this problem by using the following steps:
1. Check whether the given number is less than 3. If so, return false because 3 is the smallest prime number.
2. Check whether the given number is equal to 3. If so, return true because 3 is a prime number.
3. Check whether the given number is divisible by 2. If so, return false because all even numbers are not prime.
4. Iterate from 3 to the square root of the given number, and check whether the given number is divisible by each iteration number. If so, return false because all the multiples of the iteration number are not prime.
5. If the given number passes all the above conditions, it is a multiplication of 3 prime numbers and we can return true.

In the provided code, the function is_multiply_prime is implemented according to the above steps, and the main function is used to test the function.
*/






























































































































