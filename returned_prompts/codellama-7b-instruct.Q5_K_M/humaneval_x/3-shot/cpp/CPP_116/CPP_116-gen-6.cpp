    struct mystruct{
    int dec;
    int ones;
    };
    vector<mystruct> v;
    int i;
    for (i=0;i<arr.size();i++)
    {
        int dec=arr[i];
        int ones=0;
        while (dec>0)
        {
            dec=dec/2;
            ones+=dec%2;
        }
        mystruct m;
        m.dec=arr[i];
        m.ones=ones;
        v.push_back(m);
    }
    sort(v.begin(),v.end(),[](const mystruct& a, const mystruct& b)->bool{
        if (a.ones<b.ones)
        return true;
        if (a.ones==b.ones)
        return a.dec<b.dec;
        return false;
    });
    vector<int> final_arr;
    for (i=0;i<v.size();i++)
    final_arr.push_back(v[i].dec);
    return final_arr;
}



