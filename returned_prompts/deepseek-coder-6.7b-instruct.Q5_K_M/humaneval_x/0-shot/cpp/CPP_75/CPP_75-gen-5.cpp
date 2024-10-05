    int counter = 0, i, j, flag;
    for(i = 2; i <= a; ++i){
        if(a % i == 0){
            flag = 0;
            for(j = 2; j <= i / 2; ++j){
                if(i % j == 0){
                    flag = 1;
                    break;
                }
            }
            if(flag == 0){
                ++counter;
            }
        }
    }
    if(counter >= 3)
        return true;
    else
        return false;
}

int main(){
    int a;
    printf("Enter a number: ");
    scanf("%d", &a);
    if(is_multiply_prime(a) == true)
        printf("%d is a multiplication of 3 prime numbers\n", a);
    else
        printf("%d is not a multiplication of 3 prime numbers\n", a);
    return 0;
}

This program will check if given number is a multiplication of 3 prime numbers or not. It will return true if the number is a multiplication of 3 prime numbers otherwise false.

It will check each number from 2 to given number. If the number is a factor of the given number then it will check if the number is prime or not. If the number is prime then it will increase the counter by 1. Finally, it will check if the counter is greater than or equal to 3 then it will return true otherwise false.
*/

//