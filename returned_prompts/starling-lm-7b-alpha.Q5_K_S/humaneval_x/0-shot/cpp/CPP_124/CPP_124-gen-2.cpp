    if(date.size()==0)return false;
    int month=date[0]-'0';
    int day=date[3]-'0';
    int year=date[7]-'0';
    year=year*10+date[8]-'0';
    year=year*10+date[9]-'0';
    if(month>12 || month<1)return false;
    if(year<1000||year>3000)return false;
    if(month==2){
        if(day>29)return false;
    }else if(month==4||month==6||month==9||month==11){
        if(day>30)return false;
    }else{
        if(day>31)return false;
    }
    return true;
}

int main()
{
    char s[30];
    while(~scanf("%s",s)){
        if(valid_date(s)){
            printf("true\n");
        }else{
            printf("false\n");
        }
    }
    return 0;
}


*/






































































































































































































































