    if(date.empty()){
        return false;
    }
    if(date.size()!=10)
        return false;
    if(date[5]!='-')
        return false;
    if(date[2]!=date[5])
        return false;
    int m = (date[0]-'0') * 10 + (date[1]-'0');
    int d = (date[3]-'0') * 10 + (date[4]-'0');
    int y = (date[6]-'0') * 1000 + (date[7]-'0') * 100 + (date[8]-'0') * 10 + (date[9]-'0');
    if(m<1||m>12) return false;
    if(d<1||d>31) return false;
    if(m==2){
        if(d==30||d==31) return false;
    }
    if(m==4||m==6||m==9||m==11){
        if(d<1||d>30) return false;
    }
    if(y<1||y>3000) return false;
    return true;
}
int main(){
    string date;
    while(cin>>date){
        if(valid_date(date)) cout<<"true"<<endl;
        else cout<<"false"<<endl;
    }
    return 0;
}


















































































































































