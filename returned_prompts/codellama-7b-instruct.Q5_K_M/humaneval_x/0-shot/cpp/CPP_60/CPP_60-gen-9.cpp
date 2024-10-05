    if(n==1){
        return 1;
    }
    else{
        return (n+sum_to_n(n-1));
    }
}
int main(){
    int a;
    scanf("%d",&a);
    printf("%d",sum_to_n(a));
}
