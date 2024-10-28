    int num_apples=0;
    int num_oranges=0;
    int i;
    int num_mango;
    for (i=0;i<s.length();i++)
    {
        if (s[i]=='1' && s[i+1]==' ')
        {
            i++;
            while (s[i]<'0'||s[i]>9)i++;
            while (s[i]<='9')i++;
            num_apples=atoi(&s[i-1]);
            break;
        }
    }
    for (i=s.length()-1;i>=0;i--)
    {
        if (s[i]=='1' && s[i-1]==' ')
        {
            i--;
            while (s[i]<'0'||s[i]>9)i--;
            while (s[i]>='0')i--;
            num_oranges=atoi(&s[i+1]);
            break;
        }
    }
    num_mango=n-num_apples-num_oranges;
    return num_mango;
}  



