    string result;
    string temp;
    for (int i=0;i<message.length();i++)
    {
        if (isalpha(message[i]))
        {
            if (isupper(message[i]))
            {
                result+=tolower(message[i]);
            }
            else
            {
                result+=toupper(message[i]);
            }
        }
        else
        {
            result+=message[i];
        }
    }
    int i=0;
    while (i<result.length())
    {
        if (isalpha(result[i]))
        {
            if (result[i]=='a')
            {
                result[i]=result[i+2];
                i+=2;
            }
            if (result[i]=='e')
            {
                result[i]=result[i+2];
                i+=2;
            }
            if (result[i]=='i')
            {
                result[i]=result[i+2];
                i+=2;
            }
            if (result[i]=='o')
            {
                result[i]=result[i+2];
                i+=2;
            }
            if (result[i]=='u')
            {
                result[i]=result[i+2];
                i+=2;
            }
            if (result[i]=='A')
            {
                result[i]=result[i+2];
                i+=2;
            }
            if (result[i]=='E')
            {
                result[i]=result[i+2];
                i+=2;
            }
            if (result[i]=='I')
            {
                result[i]=result[i+2];
                i+=2;
            }
            if (result[i]=='O')
            {
                result[i]=result[i+2];
                i+=2;
            }
            if (result[i]=='U')
            {
                result[i]=result[i+2];
                i+=2;
            }
        }