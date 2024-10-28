    int i;
    int length=0;
    string result;
    for (i=0;i<strings.size();i++)
    {
        if (strings[i].length()>length)
        {
        length=strings[i].length();
        result=strings[i];
        }
    }
    return result;
}


