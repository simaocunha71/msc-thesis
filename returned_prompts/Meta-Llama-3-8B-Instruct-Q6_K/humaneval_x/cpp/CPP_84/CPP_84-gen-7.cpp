    string s = to_string(N);
    int sum = 0;
    for(int i = 0; i < s.length(); i++)
    {
        sum += s[i] - '0';
    }
    return sum;
}
int main(){
    int N;
    scanf("%d", &N);
    printf("%s", solve(N).c_str());
    return 0;
}
