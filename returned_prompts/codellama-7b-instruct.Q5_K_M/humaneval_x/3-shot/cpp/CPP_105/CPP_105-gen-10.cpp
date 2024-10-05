    vector<int> ret;
    map<int,string> map;
    map[1] = "One";
    map[2] = "Two";
    map[3] = "Three";
    map[4] = "Four";
    map[5] = "Five";
    map[6] = "Six";
    map[7] = "Seven";
    map[8] = "Eight";
    map[9] = "Nine";
    for (int i=0;i<arr.size();i++)
    {
        if (arr[i]>0 && arr[i]<10)
        ret.push_back(arr[i]);
    }
    sort(ret.begin(),ret.end());
    reverse(ret.begin(),ret.end());
    for (int i=0;i<ret.size();i++)
    {
        if (map.find(ret[i])!=map.end())
        arr[i]=map[ret[i]];
    }
    return arr;
}


