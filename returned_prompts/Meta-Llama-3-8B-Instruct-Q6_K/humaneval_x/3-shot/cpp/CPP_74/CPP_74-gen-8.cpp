    vector<string> result;
    int total_chars1=0,total_chars2=0;
    for (int i=0;i<lst1.size();i++)
    {
        total_chars1+=lst1[i].length();
    }
    for (int i=0;i<lst2.size();i++)
    {
        total_chars2+=lst2[i].length();
    }
    if (total_chars1<total_chars2)
    {
        result=lst1;
    }
    else if (total_chars1==total_chars2)
    {
        result=lst1;
    }
    else
    {
        result=lst2;
    }
    return result;
}