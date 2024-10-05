    int count=0;
    for(int i=0; i<s.length(); i+=2){
        if(s[i]=='A' || s[i]=='E' || s[i]=='I' || s[i]=='O' || s[i]=='U'){
            count++;
        }
    }
    return count;
}
int main(){
    printf("%d\n", count_upper("aBCdEf")); // returns 1
    printf("%d\n", count_upper("abcdefg")); // returns 0
    printf("%d\n", count_upper("dBBE")); // returns 0
    return 0;
}
```

## 3.1.2. 字符串操作

