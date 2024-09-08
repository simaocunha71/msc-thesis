    int i;
    for(i=n-1; i>1; i--){
        if(n%i==0)
            return i;
    }
    return 1;
}

int main()
{
    int n;
    printf("Enter a number: ");
    scanf("%d", &n);
    printf("The largest divisor is: %d\n", largest_divisor(n));
    return 0;
}

