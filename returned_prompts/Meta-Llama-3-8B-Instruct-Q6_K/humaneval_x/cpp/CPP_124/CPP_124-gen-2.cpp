    // Split the date string into month, day and year
    string month,day,year;
    size_t pos = date.find('-');
    month = date.substr(0, pos);
    date = date.substr(pos+1);
    pos = date.find('-');
    day = date.substr(0, pos);
    year = date.substr(pos+1);

    // Check if the date string is not empty
    if(month.empty() || day.empty() || year.empty())return false;

    // Convert month, day and year to integer
    int mon = stoi(month);
    int dy = stoi(day);
    int yr = stoi(year);

    // Check if the month is not less than 1 or higher than 12
    if(mon<1 || mon>12)return false;

    // Check if the day is not less than 1 or higher than 31 for months 1,3,5,7,8,10,12
    if(mon==1 || mon==3 || mon==5 || mon==7 || mon==8 || mon==10 || mon==12){
        if(dy<1 || dy>31)return false;
    }
    // Check if the day is not less than 1 or higher than 30 for months 4,6,9,11
    else if(mon==4 || mon==6 || mon==9 || mon==11){
        if(dy<1 || dy>30)return false;
    }
    // Check if the day is not less than 1 or higher than 29 for the month 2
    else if(mon==2){
        if(yr%4==0 && yr%100!=0){
            if(dy<1 || dy>29)return false;
        }
        else if(yr%4!=0){
            if(dy<1 || dy>28)return false;
        }
    }

    // Check if the date is in the format: mm-dd-yyyy
    if(month.length()>2 || day.length()>2 || year.length()>4){
        return false;
    }

    return true;
}

int main()
{
    cout<<valid_date("03-11-2000")<<endl;
    cout<<valid_date("15-01-2012")<<endl;
    cout<<valid_date("04-0-2040")<<endl;
    cout<<valid_date("06-04-2020")<<endl;
    cout<<valid_date("06/04/2020")