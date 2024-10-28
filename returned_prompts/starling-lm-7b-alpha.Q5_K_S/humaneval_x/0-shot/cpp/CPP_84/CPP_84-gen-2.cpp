    if(N==0) return "";
    int d = N%2;
    string S = solve(N/2);
    if(d==1) S = "1" + S;
    else S = "0" + S;
    return S;
}
int main(){
    int N; scanf("%d", &N);
    string S = solve(N);
    printf("%s\n", S.c_str());
    return 0;
}

*/


































































































