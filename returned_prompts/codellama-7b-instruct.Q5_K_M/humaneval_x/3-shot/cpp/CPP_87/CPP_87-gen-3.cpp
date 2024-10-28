    vector<vector<int>> all_coordinates;
    int i,j;
    for (i=0;i<lst.size();i++)
    {
        for (j=0;j<lst[i].size();j++)
        {
            if (lst[i][j]==x)
            {
                vector<int> temp;
                temp.push_back(i);
                temp.push_back(j);
                all_coordinates.push_back(temp);
            }
        }
    }
    sort(all_coordinates.begin(),all_coordinates.end(),[](vector<int>& a, vector<int>& b){
        if (a[0]==b[0])
        return a[1]>b[1];
        return a[0]<b[0];
    });
    return all_coordinates;
}





