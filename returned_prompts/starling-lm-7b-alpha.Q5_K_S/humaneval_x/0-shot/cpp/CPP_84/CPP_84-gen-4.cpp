    if(N == 0){
        return "";
    }
    int M = N % 2;
    return solve(N / 2) + to_string(M);
}

int main(){
    int N;
    scanf("%d",&N);
    string S = solve(N);
    for(int i = S.size() - 1;i >= 0;i--){
        printf("%c",S[i]);
    }
    printf("\n");
    return 0;
}


/*

Given a positive integer N, return the total sum of its digits in binary.

Example
    For N = 1000, the sum of digits will be 1 the output should be "1".
    For N = 150, the sum of digits will be 6 the output should be "110".
    For N = 147, the sum of digits will be 12 the output should be "1100".

Variables:
    @N integer
         Constraints: 0 ≤ N ≤ 10000.
Output:
     a string of binary number

*/











































































































































































































































