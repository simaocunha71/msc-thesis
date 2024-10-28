    if(date.length()!=10)
    return false;
    int m=date[0]-'0';
    int d=date[3]-'0';
    int y=date[6]-'0';
    if(m<1||m>12||d<1||d>31||y<0)
    return false;
    if(m==1||m==3||m==5||m==7||m==8||m==10||m==12){
        if(d>31)
        return false;
    }
    else if(m==4||m==6||m==9||m==11){
        if(d>30)
        return false;
    }
    else if(m==2){
        if(d>29)
        return false;
    }
    if(y<0)
    return false;
    return true;
}

int main(){
    string date;
    while(cin>>date){
        if(valid_date(date))
        printf("true\n");
        else
        printf("false\n");
    }
    return 0;
}







































































































































































































































