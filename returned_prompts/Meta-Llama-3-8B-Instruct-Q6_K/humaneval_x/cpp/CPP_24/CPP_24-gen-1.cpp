    int i;
    for(i=n-1; i>0; i--){
        if(n%i == 0) return i;
    }
    return 1;
}

int main(){
    int num;
    printf("Enter a number: ");
    scanf("%d",&num);
    printf("Largest divisor is %d\n",largest_divisor(num));
    return 0;
}

