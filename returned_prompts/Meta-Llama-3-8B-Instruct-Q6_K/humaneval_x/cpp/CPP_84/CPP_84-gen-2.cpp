    string binary = "";
    int sum = 0;
    while(N > 0){
        int rem = N % 2;
        binary = to_string(rem) + binary;
        sum += rem;
        N = N / 2;
    }
    return binary;
}
int main(){
    int N;
    printf("Enter the number: ");
    scanf("%d", &N);
    printf("Binary representation: %s\n", solve(N).c_str());
    return 0;
}

