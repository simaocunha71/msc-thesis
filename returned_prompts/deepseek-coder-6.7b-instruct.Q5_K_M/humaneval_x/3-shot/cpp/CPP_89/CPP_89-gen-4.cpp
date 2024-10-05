    string result = "";
    int length = s.length();
    for (int i=0; i<length; i++)
    {
        if (isupper(s[i]))
            result += char(int(s[i]+4-65)%26 +65);
        else
            result += char(int(s[i]+4-97)%26 +97);
    }
    return result;
}


