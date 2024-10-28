    if(date.size()==0) return false;
    int mon=date[0]*10+date[1]-'0';
    int day=date[3]*10+date[4]-'0';
    int year=date[7]*1000+date[8]*100+date[9]*10+date[10]-'0';
    if(mon>12||mon<1) return false;
    if(day>31||day<1||(mon==2&&day>28)) return false;
    if(mon==2&&day==29&&!isLeapYear(year)) return false;
    if(mon==4||mon==6||mon==9||mon==11&&day>30) return false;
    if(mon==4||mon==6||mon==9||mon==11&&day<1) return false;
    if(year%400==0||(year%4==0&&year%100!=0)) return true;
    else return false;
}
bool isLeapYear(int year){
    if(year%400==0) return true;
    if(year%100==0) return false;
    if(year%4==0) return true;
    else return false;
}
int main(){
    string date;
    cin>>date;
    if(valid_date(date)) printf("true\n");
    else printf("false\n");
}






















*/




































































































































