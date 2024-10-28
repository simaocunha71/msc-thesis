    vector<int> result;
    int i = 1;
    while (i != 1){
        i = n;
        while (i%2 == 0)
            i = i/2;
        if (i%2 != 0)
            result.push_back(i);
        while (i%2 == 0)
            i = i/2;
        if (i%2 != 0)
            i = 3*i + 1;
    }
    sort(result.begin(), result.end());
    return result;
}
