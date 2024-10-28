    vector<int> temp;
    temp=array;
    int sum=temp[0]+temp[temp.size()-1];
    if (sum%2==0)
    sort(temp.begin(),temp.end(),greater<int>());
    else
    sort(temp.begin(),temp.end());
    return temp;
}

