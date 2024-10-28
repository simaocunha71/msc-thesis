    vector<int> temp;
    vector<string> ans;
    map<int,string> mp;
    mp[1]="One";
    mp[2]="Two";
    mp[3]="Three";
    mp[4]="Four";
    mp[5]="Five";
    mp[6]="Six";
    mp[7]="Seven";
    mp[8]="Eight";
    mp[9]="Nine";
    int i;
    for (i=0;i<arr.size();i++)
        if (arr[i]>0 && arr[i]<10)
            temp.push_back(arr[i]);
    sort(temp.begin(),temp.end());
    reverse(temp.begin(),temp.end());
    for (i=0;i<temp.size();i++)
        ans.push_back(mp[temp[i]]);
    return ans;
}