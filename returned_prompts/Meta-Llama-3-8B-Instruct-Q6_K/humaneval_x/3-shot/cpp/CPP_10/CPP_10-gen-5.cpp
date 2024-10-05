    string s(str);
    string reverse_str(s);
    int i;
    for(i=str.length()-1;i>=0;i--)
    {
        if(s[i]==reverse_str[0])
        {
            reverse_str.erase(0,1);
            break;
        }
    }
    return s+reverse_str;
} 

