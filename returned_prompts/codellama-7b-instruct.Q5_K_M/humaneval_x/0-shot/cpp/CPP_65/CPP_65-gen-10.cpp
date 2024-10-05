/*
Circular shift the digits of the integer x, shift the digits right by shift
and return the result as a string.
If shift > number of digits, return digits reversed.
*/
    int len=0;
    int i=0;
    int j=0;
    int k=0;
    int temp=0;
    int flag=0;
    int flag2=0;
    string str;
    int n;
    if(shift>x)
    {
        str=to_string(x);
        reverse(str.begin(),str.end());
        return str;
    }
    else
    {
        while(x>0)
        {
            len++;
            x/=10;
        }
        if(shift>=len)
        {
            str=to_string(x);
            reverse(str.begin(),str.end());
            return str;
        }
        else
        {
            str=to_string(x);
            len=str.length();
            for(i=0;i<len;i++)
            {
                n=str[i]-'0';
                if(n!=0)
                {
                    flag=1;
                    break;
                }
            }
            if(flag==0)
            {
                str=to_string(x);
                reverse(str.begin(),str.end());
                return str;
            }
            if(flag==1)
            {
                for(i=0;i<shift;i++)
                {
                    temp=n;
                    n=str[i]-'0';
                    str[i]=temp+'0';
                }
                for(i=shift;i<len;i++)
                {
                    temp=str[i];
                    str[i]=str[i+shift];
                    str[i+shift]=temp;
                }
                for(i=0;i<len;i++)
                {
                    temp=str[i];
                    str[i]=temp+'0';
                }
                return str;
            }
        }
    }
}
