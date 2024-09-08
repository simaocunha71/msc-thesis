    int max=0;
    for(int i=0;i<lst.size();i++){
        if(lst[i]>max&&isprime(lst[i])){
            max=lst[i];
        }
    }
    int sum=0;
    while(max>0){
        sum+=max%10;
        max=max/10;
    }
    return sum;
}
int isprime(int n){
    if(n<=1) return 0;
    for(int i=2;i*i<=n;i++){
        if(n%i==0) return 0;
    }
    return 1;
}
int main() {
    vector<int> lst = {0,3,2,1,3,5,7,4,5,5,5,2,181,32,4,32,3,2,32,324,4,3};
    printf("%d\n", skjkasdkd(lst));
    return 0;
}

