    if(n==0)
        return 1;
    else if(n==1)
        return 2%p;
    else{
        int temp=modp(n/2,p);
        if(n%2==0)
            return (temp*temp)%p;
        else
            return (2*(temp*temp)%p)%p;
    }
}
int main(){
    int n,p;
    scanf("%d%d",&n,&p);
    printf("%d",modp(n,p));
    return 0;
}

The code uses recursive method to calculate power of 2 modulo p. The time complexity of the solution is O(log n).


A: The code you provided calculates the power of 2 modulo p by recursively halving n and multiplying the result with 2, modulo p, until n is 0. The function modp takes two integer arguments: n and p, and returns the result of 2^n modulo p.

Here's a step-by-step explanation of the code:

1. The function modp is defined with two parameters: n and p.

2. The function checks if n is 0. If n is 0, the function returns 1, because any number to the power of 0 is 1.

3. If n is not 0, the function checks if n is 1. If n is 1, the function returns 2 modulo p, because any number to the power of 1 is that number itself.

4. If n is neither 0 nor 1, the function calls itself with n divided by 2 and p as arguments. This is a recursive step where the function is called with n halved. The result of this recursive call is stored in the variable temp.

5. The function then checks if n is even. If n is even, the function returns the square of temp modulo p, because in this case the power of 2 is simply temp squared.

6. If n is odd, the function returns twice the square of temp modulo p, because in this case the power of 2 is 2 times temp squared.

So, in summary, this code calcul