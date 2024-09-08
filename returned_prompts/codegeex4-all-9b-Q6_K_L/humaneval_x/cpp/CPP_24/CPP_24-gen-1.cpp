    for(int i=1;i<n;i++){
        if(n%i==0){
            return i;
        }
    }
    return n;
}
int main(){
    int n;
    cin>>n;
    cout<<largest_divisor(n);
    return 0;
}