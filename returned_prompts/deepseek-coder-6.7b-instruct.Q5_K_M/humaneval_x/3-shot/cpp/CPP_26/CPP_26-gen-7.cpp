    sort(numbers.begin(), numbers.end());
    vector<int>::iterator it;
    for (it=numbers.begin(); it<numbers.end()-1; it++)
    {
        if (*it==*(it+1))
        {
            numbers.erase(it);
            it--;
        }
    }
    return numbers;
}


