    vector<int> result;
    if(a>b)
        swap(a, b);
    for(int i=a; i<=b; i++)
        if(i%2==0)
            result.push_back(i);
    return result;
}


