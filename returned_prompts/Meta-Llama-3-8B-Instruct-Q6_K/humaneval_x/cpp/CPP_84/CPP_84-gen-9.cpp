    string res = "";
    while(N > 0){
        res = (N%2 == 0 ? "0" : "1") + res;
        N /= 2;
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
    printf("Enter the number: ");
    scanf("%d", &N);
    string s = solve(N);
    printf("%s\n", s.c_str());
    return 0;
}

