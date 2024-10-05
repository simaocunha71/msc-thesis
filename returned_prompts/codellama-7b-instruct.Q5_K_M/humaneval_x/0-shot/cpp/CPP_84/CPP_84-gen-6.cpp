    string result = "0";
    while(N > 0){
        int temp = N % 2;
        result = to_string(temp) + result;
        N /= 2;
    }
    return result;
}
int main(){
    int n;
    cin>>n;
    cout<<solve(n);
    return 0;
}

