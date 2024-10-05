    string encoded_message;
    char chr;
    for (int i=0;i<message.length();i++)
    {
        chr=message[i];
        if (chr=='a'||chr=='e'||chr=='i'||chr=='o'||chr=='u')
        {
            chr=chr+2;
            if (chr>'z')
            chr=chr-26;
        }
        if (chr>='A'&&chr<='Z')
        {
            chr=chr+32;
        }
        if (chr>='a'&&chr<='z')
        {
            chr=chr-32;
        }
        encoded_message+=chr;
    }
    return encoded_message;
}



