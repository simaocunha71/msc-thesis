    int count=0;
    for(int i=2; i*i<=a; i++){
        while(a%i==0){
            a/=i;
            count++;
        }
    }
    if(a>1){
        count++;
    }
    if(count==3){
        return true;
    }
    return false;
}
int main(){
    printf("%d\n", is_multiply_prime(30));
    return 0;
}
*/

//Solution:
/*
This solution checks if the given number is the multiplication of 3 prime numbers. 
It uses a loop to check each number from 2 to sqrt(a) if it's a factor of the given number. 
If it is, it divides the number by that factor and increments a counter. 
After the loop, if the remaining number is greater than 1, it increments the counter. 
Finally, it checks if the counter is equal to 3 (indicating that the given number is a multiplication of 3 prime numbers) and returns true if so. 
Otherwise, it returns false.
*/

//Code:
/*
