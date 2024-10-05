    vector<string> result;
    if (lst1.empty())
        return lst2;
    if (lst2.empty())
        return lst1;
    int sum1=0, sum2=0;
    for (int i=0;i<lst1.size();i++)
    {
        sum1+=lst1[i].length();
    }
    for (int i=0;i<lst2.size();i++)
    {
        sum2+=lst2[i].length();
    }
    if (sum1<sum2)
        return lst1;
    if (sum1>sum2)
        return lst2;
    return lst1;
}  // return the first vector as it has same number of chars as the second vector.