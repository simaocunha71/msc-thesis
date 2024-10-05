    vector<string> sorted_vector;
    vector<string> sorted_list;
    vector<string> result;
    int i;
    int j;
    int length;
    int length_j;
    int count;
    length=0;
    count=0;
    for (i=0;i<lst.size();i++)
    {
        if (isalpha(lst[i][0])==0)
        {
            continue;
        }
        length=lst[i].length();
        count=0;
        for (j=0;j<lst.size();j++)
        {
            if (isalpha(lst[j][0])==0)
            {
                continue;
            }
            length_j=lst[j].length();
            if (length==length_j)
            {
                if (length_j==length)
                {
                    if (lst[i]>lst[j])
                    {
                        count+=1;
                    }
                }
            }
            if (length_j>length)
            {
                count+=1;
            }
        }
        if (count%2==0)
        {
            sorted_list.push_back(lst[i]);
        }
    }
    sort(sorted_list.begin(), sorted_list.end());
    return sorted_list;
}


