    if(date.empty()){
        return false;
    }
    if(date.find("-")==string::npos){
        return false;
    }
    int month=stoi(date.substr(0,2));
    int day=stoi(date.substr(3,2));
    int year=stoi(date.substr(6,4));
    if(month<1||month>12){
        return false;
    }
    if(year%4==0){
        if(day<1||day>29){
            return false;
        }
    }
    else{
        if(day<1||day>28){
            return false;
        }
    }
    switch(month){
    case 1:case 3:case 5:case 7:case 8:case 10:case 12:
        if(day<1||day>31){
            return false;
        }
        break;
    case 4:case 6:case 9:case 11:
        if(day<1||day>30){
            return false;
        }
        break;
    }
    return true;
}
int main(){
    string date;
    cin>>date;
    if(valid_date(date)){
        cout<<"true";
    }
    else{
        cout<<"false";
    }
    return 0;
}
