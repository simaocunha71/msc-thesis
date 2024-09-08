    sort(l.begin(), l.end());
    l.erase(unique(l.begin(), l.end()), l.end());
    return l;
}
int main()
{
    vector<int> l;
    for(int i=0;i<10;i++)
    {
        int t;
        scanf("%d",&t);
        l.push_back(t);
    }
    vector<int> ans=unique(l);
    for(int i=0;i<ans.size();i++)
    {
        printf("%d ",ans[i]);
    }
    return 0;
}
