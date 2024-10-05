    int max_nega=0;
    int min_posi=0;
    for (int i=0;i<lst.size();i++)
    {
        if (lst[i]<0&&lst[i]>max_nega)
        {
            max_nega=lst[i];
        }
        if (lst[i]>0&&lst[i]<min_posi)
        {
            min_posi=lst[i];
        }
    }
    vector<int> ans{max_nega,min_posi};
    return ans;
}



