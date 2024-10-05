    vector<string> result;
    int count1=0;
    int count2=0;
    for (int i=0;i<lst1.size();i++)
    {
        count1+=lst1[i].length();
    }
    for (int i=0;i<lst2.size();i++)
    {
        count2+=lst2[i].length();
    }
    if (count1<count2)
    {
        return lst1;
    }
    else if (count2<count1)
    {
        return lst2;
    }
    else
    {
        return lst1;
    }
}  // end total_match


