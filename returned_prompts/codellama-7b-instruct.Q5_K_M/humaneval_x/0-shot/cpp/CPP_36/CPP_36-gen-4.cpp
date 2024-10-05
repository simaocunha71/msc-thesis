    if(n>7){
        return 0;
    }
    else{
        return 1;
    }
}
int main()
{
    int n=0;
    scanf("%d",&n);
    printf("%d",fizz_buzz(n));
}
