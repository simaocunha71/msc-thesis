    sort(numbers.begin(), numbers.end());
    for (vector<int>::iterator it = numbers.begin(); it != numbers.end();)
    {
        if ((it+1)!=numbers.end() && *it == *(it+1)) 
        {
            numbers.erase(it);
        }
        else
        {
            ++it;
        }
    }
    return numbers;
}

