    if(N == 0)
        return "0";
    string res = "";
    while(N > 0){
        res += N % 2 + '0';
        N /= 2;
    }
    reverse(res.begin(), res.end());
    return res;
}
int main()
{
    int t;
    cin >> t;
    while(t--){
        int N;
        cin >> N;
        printf("%s\n", solve(N).c_str());
    }
    return 0;
}
