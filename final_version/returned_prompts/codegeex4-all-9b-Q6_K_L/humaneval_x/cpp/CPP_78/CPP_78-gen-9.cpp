    int i=0;
    int sum=0;
    while(num[i]!='\0'){
        if(num[i]=='2'||num[i]=='3'||num[i]=='5'||num[i]=='7'||num[i]=='B'||num[i]=='D'){
            sum++;
        }
        i++;
    }
    return sum;
}
int main(){
    string num="AB";
    printf("%d",hex_key(num));
    return 0;
}
请问这段代码是否存在错误
