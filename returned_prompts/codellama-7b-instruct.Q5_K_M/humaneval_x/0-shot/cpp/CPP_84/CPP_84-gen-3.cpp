    if(N==0) return "0";
    string res="";
    while(N>0){
        res=to_string(N%2)+res;
        N/=2;
    }
    return res;
}
int main(){
    int N;
    scanf("%d",&N);
    printf("%s",solve(N).c_str());
    return 0;
}