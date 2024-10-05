    if(num[0]>='0'&&num[0]<='9'){
        if(num[0]=='0'||num[0]=='1'||num[0]=='4'||num[0]=='6'||num[0]=='9')
            return 0;
        else
            return 1;
    }
    else if(num[0]=='A')
        return 2;
    else if(num[0]=='B')
        return 3;
    else if(num[0]=='C')
        return 4;
    else if(num[0]=='D')
        return 5;
    else if(num[0]=='E')
        return 6;
    else if(num[0]=='F')
        return 7;
    else{
        printf("ERROR");
        goto A;
    }
}

int main(){
    string num;
    while(cin>>num){
        int sum=0;
        for(int i=0;i<num.size();i++)
            if(hex_key(num[i]))
                sum++;
        printf("%d\n",sum);
    }
    return 0;
}

*/
















































































































































































































