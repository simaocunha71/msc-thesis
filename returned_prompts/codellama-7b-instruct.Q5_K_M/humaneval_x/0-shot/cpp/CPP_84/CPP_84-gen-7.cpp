    if(N==0) return "0";
    int num = N%2;
    N /= 2;
    goto A;
}
int main(){
    int N = 150;
    printf("%s",solve(N).c_str());
    return 0;
}

