    for(int i=n-1; i>0; i--){
        if(n%i==0){
            return i;
        }
    }
}
int main() {
    int num;
    printf("Enter a number: ");
    scanf("%d",&num);
    printf("The largest divisor of %d is: %d",num, largest_divisor(num));
    return 0;
}

*/

/*

