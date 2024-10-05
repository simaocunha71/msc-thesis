    if(N==0){
        return "0";
    }
    int k=N%2;
    N=N/2;
    goto A;
}
int main(){
    int N;
    scanf("%d",&N);
    printf("%s",solve(N).c_str());
    return 0;
}
