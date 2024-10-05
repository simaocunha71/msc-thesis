    vector<int>::iterator it;
    for (it=numbers.begin();it!=numbers.end();it++)
    {
        int num=*it;
        it=find(numbers.begin(),it,num);
        if (it!=numbers.end())
        {
            numbers.erase(it);
        }
    }
    return numbers;
}


