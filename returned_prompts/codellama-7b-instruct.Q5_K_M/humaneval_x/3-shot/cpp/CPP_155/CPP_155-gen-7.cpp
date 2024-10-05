    vector<int> result;
    string temp=to_string(num);
    int len=temp.length();
    int count=0;
    for (int i=0;i<len;i++)
    if (temp[i]%2==0)
    count+=1;
    result.push_back(count);
    count=0;
    for (int i=0;i<len;i++)
    if (temp[i]%2!=0)
    count+=1;
    result.push_back(count);
    return result;
}



