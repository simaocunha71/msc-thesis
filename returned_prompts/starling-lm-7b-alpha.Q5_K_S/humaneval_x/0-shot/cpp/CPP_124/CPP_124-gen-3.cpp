    if(date.length()!=10)
    {
        return false;
    }
    if(date[2]!='-'||date[5]!='-')
    {
        return false;
    }
    int month=date[0]-'0';
    int day=date[3]-'0';
    int year=date[6]-'0';
    year+=10*date[7]-'0';
    year+=100*(date[8]-'0');
    year+=1000*(date[9]-'0');
    if(year<1900)
    {
        return false;
    }
    if(month>12)
    {
        return false;
    }
    if(month==2)
    {
        if(day<1||day>29)
        {
            return false;
        }
    }
    if(month==4||month==6||month==9||month==11)
    {
        if(day<1||day>30)
        {
            return false;
        }
    }
    if(month==1||month==3||month==5||month==7||month==8||month==10)
    {
        if(day<1||day>31)
        {
            return false;
        }
    }
    return true;
}
int main()
{
    string date="03-11-2000";
    if(valid_date(date))
    {
        printf("The date is valid");
    }
    else
    {
        printf("The date is invalid");
    }
    return 0;
}




































































































