    if(n==1){
        return 1;
    }
    else if(n%2==0){
        n=n/2;
        goto A;
    }
    else{
        n=n-1;
        goto A;
    }
}

int main(){
    int n=15;
    printf("%d",largest_divisor(n));
    return 0;
}
