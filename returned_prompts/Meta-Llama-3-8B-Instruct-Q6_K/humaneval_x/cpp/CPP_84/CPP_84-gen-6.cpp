    // your code goes here
    string res = "";
    while(N > 0){
        int r = N % 2;
        res = to_string(r) + res;
        N = N / 2;
    }
    int sum = 0;
    for(int i = 0; i < res.length(); i++){
        sum += res[i] - '0';
    }
    return res;
}

int main()
{
    int N;
    cin >> N;
    cout << solve(N) << endl;
    return 0;
}

