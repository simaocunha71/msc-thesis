    if (N == 1) return "1";
    if (N == 0) return "0";
    int res = 0;
    while (N > 0) {
        int mod = N % 2;
        res += mod;
        N /= 2;
    }
    return to_string(res);
}

int main(){
    int N;
    cin >> N;
    cout << solve(N) << endl;
    return 0;
}
