    if(date.size() != 10)
        return false;
    if(date[2] != '-' || date[5] != '-')
        return false;

B:
    string month = date.substr(0, 2);
    string day = date.substr(3, 2);
    string year = date.substr(6, 4);

    if(stoi(month) < 1 || stoi(month) > 12)
        return false;

C:
    int days;
    if(stoi(month) == 2){
        days = 29;
    }
    else if((stoi(month)%2) != 0){
        days = 31;
    }
    else if((stoi(month)%2) == 0 && stoi(month) != 2 && stoi(month) != 12){
        days = 30;
    }
    else if(stoi(month) == 12){
        days = 30;
    }
    else{
        return false;
    }

D:
    if(stoi(day) < 1 || stoi(day) > days)
        return false;

E:
    return true;
}
int main(){
    printf("%d\n", valid_date("03-11-2000"));
    printf("%d\n", valid_date("15-01-2012"));
    printf("%d\n", valid_date("04-0-2040"));
    printf("%d\n", valid_date("06-04-2020"));
    printf("%d\n", valid_date("06/04/2020"));
    return 0;
}
*/

