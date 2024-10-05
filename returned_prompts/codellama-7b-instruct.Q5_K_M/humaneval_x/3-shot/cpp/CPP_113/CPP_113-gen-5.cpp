    vector<string> odd_elements;
    map<string,int> odd_counts;
    string odd_count;
    int i;
    int length;
    for (i=0;i<lst.size();i++)
    {
        length=lst[i].length();
        for (int j=0;j<length;j++)
        {
            if (lst[i][j]%2!=0)
            {
                odd_count+=lst[i][j];
            }
        }
        odd_elements.push_back(odd_count);
        odd_count="";
    }
    return odd_elements;
}

