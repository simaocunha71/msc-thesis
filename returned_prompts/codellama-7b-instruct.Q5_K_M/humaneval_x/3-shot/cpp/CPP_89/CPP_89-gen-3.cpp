    string encrypted_string;
    int i;
    int chr;
    for (i=0;i<s.length();i++)
    {
        chr=s[i];
        if (chr>='a' && chr<='z')
        {
            if (chr-'a'<26)
            encrypted_string+=chr+2*(chr-'a');
            else
            encrypted_string+=chr-26+(chr-'a');
        }
        else if (chr>='A' && chr<='Z')
        {
            if (chr-'A'<26)
            encrypted_string+=chr+2*(chr-'A');
            else
            encrypted_string+=chr-26+(chr-'A');
        }
        else
        {
            encrypted_string+=chr;
        }
    }
    return encrypted_string;
}


