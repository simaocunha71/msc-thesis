    int i;
    int length = s.length();
    string new_string;
    for (i=0;i<length;i++)
    {
        if (s[i]==' ')
        {
            new_string+=' ';
        }
        else
        {
            new_string+=*max_element(s.begin(),s.end());
            s.erase(s.begin());
        }
    }
    return new_string;
}


