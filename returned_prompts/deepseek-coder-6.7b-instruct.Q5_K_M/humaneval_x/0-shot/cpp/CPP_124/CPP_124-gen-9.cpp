    if(date.empty() || date.length() != 10 || date[2] != '-' || date[5] != '-') 
        return false;

B:
    int month = stoi(date.substr(0,2));
    int day = stoi(date.substr(3,2));
    int year = stoi(date.substr(6,4));

C:
    if(month < 1 || month > 12 || day < 1 || year < 1)
        return false;

D:
    if(month == 2){
        if(day > 29) 
            return false;
    } 
    else if(month == 4 || month == 6 || month == 9 || month == 11){
        if(day > 30)
            return false;
    }
    else{
        if(month == 1 || month == 3 || month == 5 || month == 7 || month == 8 || month == 10 || month == 12){
            if(day > 31) 
                return false;
        }
    }

E:
    return true;
}

int main(){
    string test1 = "03-11-2000";
    string test2 = "15-01-2012";
    string test3 = "04-0-2040";
    string test4 = "06-04-2020";
    string test5 = "06/04/2020";

    printf("%s => %s\n", test1.c_str(), valid_date(test1) ? "true" : "false");
    printf("%s => %s\n", test2.c_str(), valid_date(test2) ? "true" : "false");
    printf("%s => %s\n", test3.c_str(), valid_date(test3) ? "true" : "false");
    printf("%s => %s\n", test4.c_str(), valid_date(test4) ? "true" : "false");
    printf("%s => %s\n", test5.c_str(), valid_