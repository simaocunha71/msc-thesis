    string encoded_message;
    string::iterator it;
    for(it=message.begin();it!=message.end();it++)
    {
        if (isalpha(*it))
        {
            if (islower(*it))
            {
                if (*it=='a'||*it=='e'||*it=='i'||*it=='o'||*it=='u')
                {
                if (*it=='a')
                encoded_message+=char(*it+2);
                else
                encoded_message+=char(*it+1);
                }
                else
                encoded_message+=char(*it+1);
            }
            else
            {
                if (*it=='A'||*it=='E'||*it=='I'||*it=='O'||*it=='U')
                {
                if (*it=='A')
                encoded_message+=char(*it+2);
                else
                encoded_message+=char(*it+1);
                }
                else
                encoded_message+=char(*it-1);
            }
        }
        else
        encoded_message+=*it;
    }
    return encoded_message;
}



