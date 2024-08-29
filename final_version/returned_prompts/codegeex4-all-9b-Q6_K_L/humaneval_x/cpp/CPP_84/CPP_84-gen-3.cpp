    string ans = "";
    int sum = 0;
    while(N){
        sum += N % 2;
        N /= 2;
    }
    while(sum){
        ans += to_string(sum % 2);
        sum /= 2;
    }
    reverse(ans.begin(), ans.end());
    return ans;

B:
    string ans = "";
    while(N){
        ans += to_string(N % 2);
        N /= 2;
    }
    reverse(ans.begin(), ans.end());
    return ans;
}
int main(){
    int N;
    cin >> N;
    cout << solve(N) << endl;
    return 0;
}
