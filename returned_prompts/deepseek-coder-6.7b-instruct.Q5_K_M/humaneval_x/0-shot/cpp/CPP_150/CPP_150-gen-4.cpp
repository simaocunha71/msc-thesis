    int i, flag = 0;

    for(i = 2; i <= n/2; ++i){
        if(n % i == 0){
            flag = 1;
            break;
        }
    }

    if (flag == 1)
        return y;
    else
        return x;
}

int main(){
    printf("%d", x_or_y(7, 34, 12));
    return 0;
}
*/

S:
/*
Here is a simple solution to the problem. The function x_or_y is checking if the number n is a prime number or not. If it is a prime number, it returns the value of x otherwise it returns the value of y.

In the function x_or_y, we start a loop from 2 to n/2. If the number n is divisible by any number in this range, it is not a prime number and we return y. If n is not divisible by any number in this range, it is a prime number and we return x.

In the main function, we call x_or_y function with the values 7, 34, 12 and print the returned value.
*/

int main(){
    printf("%d", x_or_y(7, 34, 12));
    return 0;
}

*/

*/


/*

