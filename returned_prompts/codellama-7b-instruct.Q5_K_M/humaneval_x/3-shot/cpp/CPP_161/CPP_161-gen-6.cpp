    string new_s;
    bool flag=false;
    for (int i=0;i<s.length();i++)
    {
        if (isalpha(s[i])){
            if (islower(s[i]))
            new_s+=(char)toupper(s[i]);
            else
            new_s+=(char)tolower(s[i]);
        }
        else{
            new_s+=s[i];
        }
    }
    if (flag==false)
    return new_s;
    return reverse(new_s.begin(), new_s.end());
}



