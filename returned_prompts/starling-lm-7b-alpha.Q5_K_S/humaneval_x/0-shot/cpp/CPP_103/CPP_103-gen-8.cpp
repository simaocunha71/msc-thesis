    if(n>m) return "-1";
    int tmp = (n+m)/2;
    string res = to_string(tmp);
    while(res.size()!=4) res = "0"+res;
    return res;
}

int main() {
    int n,m;
    scanf("%d%d",&n,&m);
    printf("%s\n", rounded_avg(n, m).c_str());
    return 0;
}



```
