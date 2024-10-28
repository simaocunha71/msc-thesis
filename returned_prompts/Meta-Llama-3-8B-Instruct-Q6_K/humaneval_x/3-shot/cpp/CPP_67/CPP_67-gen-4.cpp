    int apples=0;
    int oranges=0;
    for(int i=0;i<s.length();i++)
    {
        if(s[i]==' ')
        {
            if(s[i-1]=='1' || s[i-1]=='2' || s[i-1]=='3' || s[i-1]=='4' || s[i-1]=='5' || s[i-1]=='6' || s[i-1]=='7' || s[i-1]=='8' || s[i-1]=='9' || s[i-1]=='0')
            {
                apples++;
            }
        }
        if(s[i]=='a' && s[i+1]=='p' && s[i+2]=='p' && s[i+3]=='l' && s[i+4]=='e' && s[i+5]=='s')
        {
            apples++;
        }
        if(s[i]=='o' && s[i+1]=='r' && s[i+2]=='a' && s[i+3]=='n' && s[i+4]=='g' && s[i+5]=='e' && s[i+6]=='s')
        {
            oranges++;
        }
    }
    return n-apples-oranges;
}
