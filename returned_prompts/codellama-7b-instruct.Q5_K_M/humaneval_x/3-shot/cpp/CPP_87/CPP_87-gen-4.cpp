    vector<vector<int>> result;
    for (int i=0;i<lst.size();i++)
    {
        for (int j=0;j<lst[i].size();j++)
        {
            if (lst[i][j]==x)
            {
                vector<int> temp;
                temp.push_back(i);
                temp.push_back(j);
                result.push_back(temp);
            }
        }
    }
    result.sort([](vector<int>&a, vector<int>&b){
    if (a[0]>b[0])
        return true;
    else if (a[0]==b[0])
        return a[1]<b[1];
    });
    return result;
}


