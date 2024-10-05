    string result;
    for (int i=0;i<message.length();i++)
    {
        char c=message[i];
        if (isupper(c))
        {
            c=tolower(c);
        }
        else if (islower(c))
        {
            c=toupper(c);
        }
        if (c=='a' || c=='e' || c=='i' || c=='o' || c=='u')
        {
            if (c=='a')
                c='c';
            else if (c=='e')
                c='g';
            else if (c=='i')
                c='k';
            else if (c=='o')
                c='q';
            else if (c=='u')
                c='w';
        }
        result+=c;
    }
    return result;
} 
