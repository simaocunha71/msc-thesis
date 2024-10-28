    int n=grid.size();
    int m=grid[0].size();
    int res=0;
    for(int i=0;i<n;i++)
        for(int j=0;j<m;j++)
            if(grid[i][j])
                res++;
    if(res%capacity==0)
        return res/capacity;
    else
        return res/capacity+1;

B:
    int n=grid.size();
    int m=grid[0].size();
    int res=0,remain=capacity;
    for(int i=0;i<n;i++)
        for(int j=0;j<m;j++)
            if(grid[i][j])
            {
                if(capacity>=grid[i][j])
                {
                    grid[i][j]=0;
                    remain-=grid[i][j];
                }
                else
                {
                    grid[i][j]-=capacity;
                    remain=capacity;
                }
                res++;
                if(remain==0)
                    continue;
            }
    if(remain)
        res++;
    return res;
}

int main()
{
    vector<vector<int>> grid={{0,0,1,0}, {0,1,0,0}, {1,1,1,1}};
    int capacity=1;
    printf("%d\n",max_fill(grid,capacity));
    return 0;
}


*/








































































































































