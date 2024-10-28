    int n=a.size();
    int m=b.size();
    string res="";
    for(int i=0;i<n;i++){
        if(a[i]==b[i])
            res+='0';
        else
            res+='1';
    }
    return res;
}

int main(){
    string a,b;
    scanf("%s",&a);
    scanf("%s",&b);
    printf("%s",string_xor(a,b).c_str());
    return 0;
}
```

## 2.1
