    string encoded;
    for (char chr : message)
    {
        if (isalpha(chr))
        {
            if (isupper(chr))
            {
                chr=tolower(chr);
            }
            else
            {
                chr=toupper(chr);
            }
            if (chr=='a' || chr=='e' || chr=='i' || chr=='o' || chr=='u')
            {
                chr=(chr+2)%26+'a';
            }
        }
        encoded+=chr;
    }
    return encoded;
} 
