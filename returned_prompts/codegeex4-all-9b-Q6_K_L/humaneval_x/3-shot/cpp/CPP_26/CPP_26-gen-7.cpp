    vector<int> new_numbers;
    vector<int> temp=numbers;
    sort(temp.begin(),temp.end());
    for (int i=0;i<temp.size();i++)
    if (temp[i]!=temp[i+1]){
        new_numbers.push_back(temp[i]);
    }
    return new_numbers;
}

