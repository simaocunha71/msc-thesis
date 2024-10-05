    vector<int> res(k);
    nth_element(arr.begin(),arr.begin()+k-1,arr.end());
    res[0]=arr[k-1];
    return res;
}


