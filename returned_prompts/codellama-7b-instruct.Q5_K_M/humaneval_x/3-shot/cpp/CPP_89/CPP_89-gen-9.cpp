    string encrypted_string;
    string alphabet="abcdefghijklmnopqrstuvwxyz";
    int i;
    for (i=0;i<s.length();i++)
    {
        if (alphabet.find(s[i])==string::npos)
        {
            encrypted_string+=s[i];
        }
        else
        {
            encrypted_string+=alphabet[((alphabet.find(s[i]))+2)*2];
        }
    }
    return encrypted_string;
}

