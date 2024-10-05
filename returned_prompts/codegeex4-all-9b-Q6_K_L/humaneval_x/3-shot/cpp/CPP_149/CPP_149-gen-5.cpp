    vector<string> newlist;
    vector<string> newlist2;
    vector<string> newlist3;
    int i,j;
    for (i=0;i<lst.size();i++)
    if (lst[i].length()%2==0)
    newlist.push_back(lst[i]);
    sort(newlist.begin(),newlist.end());
    for (j=0;j<newlist.size();j++)
    if (j==0)
    newlist2.push_back(newlist[j]);
    else if (newlist[j]!=newlist[j-1])
    newlist2.push_back(newlist[j]);
    return newlist2;

}

