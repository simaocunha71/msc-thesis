    vector<int> temp(arr.begin()+arr.size()-k,arr.end());
    sort(temp.begin(),temp.end());
    return temp;
}

