    int month,day,year;
    char chr;
    int i;
    bool valid=true;
    for (i=0;i<date.length();i++)
    {
        chr=date[i];
        if (chr=='-')
        {
            if (i==0 || i==date.length()-1)
            {
                valid=false;
                return valid;
            }
            if (i==1)
            {
                month=atoi(date.substr(0,i).c_str());
                day=atoi(date.substr(2,date.length()-2).c_str());
                year=atoi(date.substr(5,date.length()-5).c_str());
                if (month<1 || month>12)
                {
                    valid=false;
                }
                else if ((month==4 || month==6 || month==9 || month==11) && day>30)
                {
                    valid=false;
                }
                else if (month==2)
                {
                    if (day>29)
                    {
                        valid=false;
                    }
                }
                else if ((month==1 || month==3 || month==5 || month==7 || month==8 || month==10 || month==12) && day>31)
                {
                    valid=false;
                }
            }
        }
        else if (chr!='-' && chr!=' ')
        {
            valid=false;
        }
    }
    return valid;
}
//using the date string as input
int main()
{
    cout<<valid_date("03-11-2000")<<endl;
    cout<<valid_date("15-01-2012")<<endl;
    cout<<valid_date("04-0-2040")<<endl;
    cout<<valid_date("06-04-2020")<<endl;
    cout<<valid_date("06/04/2020")<<endl;
    return 0;
}
//end of main function
//end of program
//end of file
//end of code
//end of the end
//end of the end of the end
//end of the end of the end of the end
//end of the end of the end of the end of the end
//end of the end of the end of the end of the end of the end
//end of the end of the end of the end of the end of the end of the end
//end of the end of the end of the end of the end of the end of the end of the end
//end of the