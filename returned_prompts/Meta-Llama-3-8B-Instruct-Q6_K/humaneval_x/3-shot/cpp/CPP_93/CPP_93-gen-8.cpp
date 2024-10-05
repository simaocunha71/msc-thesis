    string result;
    for (int i=0;i<message.length();i++)
    {
        if (isalpha(message[i]))
        {
            char c=message[i];
            if (islower(c))
            {
                if (c=='a' || c=='e' || c=='i' || c=='o' || c=='u')
                {
                    c+=2;
                    if (c>'u')
                        c='a';
                }
                else
                    c+=2;
                if (c>'z')
                    c='a'+(c-'z'-1);
                result+=tolower(c);
            }
            else
            {
                if (c=='A' || c=='E' || c=='I' || c=='O' || c=='U')
                {
                    c+=2;
                    if (c>'U')
                        c='A';
                }
                else
                    c+=2;
                if (c>'Z')
                    c='A'+(c-'Z'-1);
                result+=toupper(c);
            }
        }
        else
            result+=message[i];
    }
    return result;
}

