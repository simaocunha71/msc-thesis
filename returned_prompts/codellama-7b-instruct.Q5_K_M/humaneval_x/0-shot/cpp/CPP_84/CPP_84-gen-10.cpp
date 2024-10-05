    if (N == 0)
        return "0";
    else{
        string s = "";
        while (N != 0){
            s = to_string(N % 2) + s;
            N /= 2;
        }
        return s;
    }
}
int main(){
    int N;
    scanf("%d", &N);
    string res = solve(N);
    cout << res << endl;
    return 0;
}
