    int n=grid.size();
    vector<int> res;
    for (int i=0;i<n;i++)
    for (int j=0;j<n;j++)
    {
        int val=grid[i][j];
        int cnt=0;
        for (int x=i-1;x<=i+1;x++)
        for (int y=j-1;y<=j+1;y++)
        if (x>=0 && y>=0 && x<n && y<n)
        {
            if (grid[x][y]!=val)
            {
                cnt++;
            }
        }
        if (cnt==k)
        {
            res.push_back(val);
        }
    }
    return res;
}