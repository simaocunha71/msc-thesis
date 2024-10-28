    if(N==0) return "0";
    string s = "";
    int r = N%2;
    N /= 2;
    s += to_string(r);
    goto A;
}
int main(){
    int N;
    cin>>N;
    cout<<solve(N);
}
