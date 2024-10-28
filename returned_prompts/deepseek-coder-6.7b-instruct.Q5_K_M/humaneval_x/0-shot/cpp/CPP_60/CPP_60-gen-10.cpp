    int i,sum=0;
    for(i=1;i<=n;i++){
        sum += i;
    }
    return sum;
}

int main(){
    int n;
    printf("Enter a number: ");
    scanf("%d",&n);
    printf("Sum from 1 to %d: %d",n,sum_to_n(n));
    return 0;
}

This is a C++ program, which prompts the user to input a number, then prints the sum of numbers from 1 to that number by using the function sum_to_n.
