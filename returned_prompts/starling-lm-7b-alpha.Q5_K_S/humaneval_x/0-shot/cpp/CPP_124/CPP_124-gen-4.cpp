    if(date=="")
    {
        return false;
    }
    else
    {
        if(date.size()!=10)
        {
            return false;
        }
        else
        {
            int m=0,d=0,y=0;
            for(int i=0;i<date.size();i++)
            {
                if(i==2||i==5)
                {
                    m+=date[i]-'0';
                }
                else if(i==5)
                {
                    d+=date[i]-'0';
                }
                else if(i==8)
                {
                    y+=date[i]-'0';
                }
                else if(i==9)
                {
                    d+=date[i]-'0';
                }
                else if(i==10)
                {
                    y+=date[i]-'0';
                }
            }
            if(m>12||m<1)
            {
                return false;
            }
            else if(d>31||d<1||(m==2&&d>29)||(m==4||m==6||m==9||m==11&&d>30))
            {
                return false;
            }
            else if(y<0||y>9999)
            {
                return false;
            }
            else
            {
                return true;
            }
        }
    }
}
int main()
{
    string date;
    cin>>date;
    if(valid_date(date))
    {
        printf("true\n");
    }
    else
    {
        printf("false\n");
    }
    return 0;
}



























































