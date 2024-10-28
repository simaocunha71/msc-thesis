    int mango=0;
    int i=0;
    while (i<s.length())
    {
        if (s[i]=='a')
        {
            int j=i+1;
            while (j<s.length() && s[j]!=' ')
            j++;
            int num=atoi(s.substr(i+1,j-i-1).c_str());
            mango+=num;
            i=j;
        }
        else if (s[i]=='o')
        {
            int j=i+1;
            while (j<s.length() && s[j]!=' ')
            j++;
            int num=atoi(s.substr(i+1,j-i-1).c_str());
            mango+=num;
            i=j;
        }
        else
        i++;
    }
    return n-mango;
}
//Note: This solution does not handle the case where the string contains extra characters. It also assumes that the input string is well-formed and does not contain any non-numeric characters. For a more robust solution, you would need to add error checking and handling for these cases.