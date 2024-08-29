    int sum=0;
    while(N>0){
        sum+=N%10;
        N/=10;
    }
    string str="";
    while(sum>0){
        str+=(sum%2)+'0';
        sum/=2;
    }
    reverse(str.begin(),str.end());
    return str;

B:
    int sum=0;
    while(N>0){
        sum+=N%10;
        N/=10;
    }
    string str=to_string(sum);
    reverse(str.begin(),str.end());
    return str;

C:
    string str="";
    while(N>0){
        str+=(N%2)+'0';
        N/=2;
    }
    reverse(str.begin(),str.end());
    return str;

D:
    int sum=0;
    while(N>0){
        sum+=N%2;
        N/=2;
    }
    string str=to_string(sum);
    reverse(str.begin(),str.end());
    return str;

E:
    int sum=0;
    while(N>0){
        sum+=N%2;
        N/=2;
    }
    string str="";
    while(sum>0){
        str+=(sum%2)+'0';
        sum/=2;
    }
    reverse(str.begin(),str.end());
    return str;

F:
    int sum=0;
    while(N>0){
        sum+=N%10;
        N/=10;
    }
    string str="";
    while(sum>0){
        str+=(sum%10)+'0';
        sum/=10;
    }
    reverse(str.begin(),str.end());
    return str;

G:
    int sum=0;
    while(N>0){
        sum+=N%10;
        N/=10;
    }
    string str="";
    while(sum>0){
        str+=(sum%2)+'0';
        sum/=2;
    }
    return str;

H:
    int sum=0;
    while(N>0){
        sum+=N%10;
        N/=10;
    }
    string str="";
    while(sum>0){
        str+=(sum%10)+'0';
        sum/=10;
    }
    reverse(str.begin(),str.end());
    return str;

I:
    int sum=0;
    while(N>0){
        sum+=N%10;
        N/=10;
    }
    string str="";
    while(sum>0){
        str+=(sum%2)+'0';
        sum/=2;
    }
    return