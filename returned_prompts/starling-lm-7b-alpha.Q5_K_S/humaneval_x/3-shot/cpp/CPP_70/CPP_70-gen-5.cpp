    vector<int> sorted;
    int size=lst.size();
    int i;
    for (i=0;i<size;i++)
    {
        int min=*min_element(lst.begin(),lst.begin()+i+1);
        int index=min_element(lst.begin(),lst.begin()+i+1)-lst.begin();
        sorted.push_back(min);
        lst.erase(lst.begin()+index);
    }
    return sorted;
}



