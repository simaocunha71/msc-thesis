    vector<string> sorted_list;
    string tmp;
    int i,j,k;
    for (i=0;i<lst.size();i++)
    if (lst[i].length()%2==0)
    sorted_list.push_back(lst[i]);

    for (i=0;i<sorted_list.size();i++)
    for (j=i+1;j<sorted_list.size();j++)
    {
        if (sorted_list[i].length()>sorted_list[j].length())
        {
        tmp=sorted_list[i];
        sorted_list[i]=sorted_list[j];
        sorted_list[j]=tmp;
        }
    }

    for (k=0;k<lst.size();k++)
    for (i=0;i<sorted_list.size();i++)
    if (lst[k].length()%2==1 && lst[k]==sorted_list[i])
    sorted_list.erase(sorted_list.begin()+i);

    sort(sorted_list.begin(), sorted_list.end());
    return sorted_list;
}

