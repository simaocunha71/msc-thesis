    vector<int> temp;
    int i;
    for (i=0;i<arr.size();i++)
    temp.push_back(arr[i]);
    sort(temp.begin(), temp.end());

    for (i=0;i<arr.size();i++)
    if (temp[i]!=arr[(i+1)%arr.size()])
    return false;

    return true;
}

