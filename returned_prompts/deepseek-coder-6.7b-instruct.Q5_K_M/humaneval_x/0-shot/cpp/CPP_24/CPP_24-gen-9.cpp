    for(int i=n-1;i>0;i--){
        if(n%i==0){
            return i;
        }
    }

}
int main(){
    int n;
    scanf("%d",&n);
    printf("%d",largest_divisor(n));
    return 0;
}

