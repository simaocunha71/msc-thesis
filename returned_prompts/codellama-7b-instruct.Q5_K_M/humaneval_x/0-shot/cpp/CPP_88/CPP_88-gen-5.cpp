    vector<int> v;
    // for(int i=0;i<array.size();i++)
    // {
    //     v.push_back(array[i]);
    // }
    // sort(v.begin(),v.end());
    // for(int i=0;i<v.size();i++)
    // {
    //     printf("%d ",v[i]);
    // }
    // printf("\n");
    // return v;
    vector<int> v1;
    for(int i=0;i<array.size();i++)
    {
        v1.push_back(array[i]);
    }
    sort(v1.begin(),v1.end());
    // for(int i=0;i<v1.size();i++)
    // {
    //     printf("%d ",v1[i]);
    // }
    // printf("\n");
    // return v1;
    vector<int> v2;
    for(int i=0;i<v1.size();i++)
    {
        v2.push_back(v1[i]);
    }
    if((v1[0]+v1[v1.size()-1])%2==0)
    {
        sort(v2.begin(),v2.end(),greater<int>());
    }
    // for(int i=0;i<v2.size();i++)
    // {
    //     printf("%d ",v2[i]);
    // }
    // printf("\n");
    // return v2;
    // printf("v2 size = %d\n",v2.size());
    vector<int> v3;
    for(int i=0;i<v2.size();i++)
    {
        v3.push_back(v2[i]);
    }
    // printf("v3 size = %d\n",v3.size());
    // return v3;
    // for(int i=0;i<v3.size();i++)
    // {
    //     printf("%d ",v3[i]);
    // }
    // printf