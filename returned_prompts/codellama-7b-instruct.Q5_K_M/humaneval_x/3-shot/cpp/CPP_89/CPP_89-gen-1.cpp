    string encrypted_string;
    int i;
    for (i=0;i<s.length();i++)
    {
        int ascii_value=s[i];
        if ((ascii_value>='a'&&ascii_value<='z')||(ascii_value>='A'&&ascii_value<='Z'))
        {
            if (ascii_value>='a'&&ascii_value<='z')
            {
                if (ascii_value=='z')
                encrypted_string+=('a');
                else
                encrypted_string+=((ascii_value-2)*2);
            }
            if (ascii_value>='A'&&ascii_value<='Z')
            {
                if (ascii_value=='Z')
                encrypted_string+=('A');
                else
                encrypted_string+=((ascii_value-2)*2);
            }
        }
        else
        encrypted_string+=s[i];
    }
    return encrypted_string;
}


