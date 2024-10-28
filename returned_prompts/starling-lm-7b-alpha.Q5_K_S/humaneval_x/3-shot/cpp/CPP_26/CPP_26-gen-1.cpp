    vector<int>::iterator it;
    for (it=numbers.begin();it!=numbers.end();it++)
    if (count(numbers.begin(),it,*(it))>1)
    numbers.erase(it);
    return numbers;
}


