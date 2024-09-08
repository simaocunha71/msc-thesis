    string s = "";
    while(N > 0){
        s = (N % 2 ? "1" : "0") + s;
        N /= 2;
    }
    int sum = 0;
    for(int i = 0; i < s.size(); i++){
        sum += s[i] - '0';
    }
    return s;

}

int main() {
    int N;
    printf("Enter a positive integer N: ");
    scanf("%d", &N);
    printf("The sum of digits in binary is: %s\n", solve(N).c_str());
    return 0;
}

E:
    1
    0
    1
    1
    0
    0
    0
    0
    0
    0
    1
    1
    1
    1
    0
    0
    0
    0
    0
    0
    0
    0
    0
    1
    0
    1
    1
    1
    1
    1
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    1
    1
    1
    1
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    1
    1
    1
    1
    1
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    1
    0
    1
    1
    1
    1
    1
    1
    0
    0
    0
    0
    0
    0
    0
    0
    0
    0
    1
    1
    1
    1
    1
    1
    0
    0