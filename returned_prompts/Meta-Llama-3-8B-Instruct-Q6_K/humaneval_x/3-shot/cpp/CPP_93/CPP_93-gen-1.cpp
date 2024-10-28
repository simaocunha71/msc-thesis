    string result;
    for (int i=0;i<message.length();i++)
    {
        char c=message[i];
        if (c>='A' && c<='Z')
        {
            c=char(c-('A'-1));
            result+=char(c);
        }
        else if (c>='a' && c<='z')
        {
            c=char(c-('a'-1));
            result+=char(c);
        }
        else
        {
            if (c=='a' || c=='e' || c=='i' || c=='o' || c=='u')
            {
                if (c=='a')
                {
                    c='c';
                }
                else if (c=='e')
                {
                    c='g';
                }
                else if (c=='i')
                {
                    c='k';
                }
                else if (c=='o')
                {
                    c='q';
                }
                else
                {
                    c='s';
                }
                result+=c;
            }
            else
            {
                result+=c;
            }
        }
    }
    for (int i=0;i<message.length();i++)
    {
        char c=message[i];
        if (c>='A' && c<='Z')
        {
            c=char(c-('A'-1));
            result+=char(c+('Z'-'a'+1));
        }
        else if (c>='a' && c<='z')
        {
            c=char(c-('a'-1));
            result+=char(c+('z'-'A'+1));
        }
        else
        {
            result+=c;
        }
    }
    return result;
}  //not working as expected
//the problem with this code is that it will replace all the vowels with 'c', 'g', 'k', 'q', 's' 
//which is not the correct logic. it should replace them with the next two letters in the alphabet. 
//for example 'a' should be replaced with 'c', 'e' with 'g', 'i' with 'k', 'o' with 'q', 'u' with 'w'. 
//similarly for lowercase vowels. 
//also the code does not swap the case correctly.  //it should swap the case of all the letters. 
//it should not convert 'A' to 'a' and vice versa. it should convert