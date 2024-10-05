    vector<int> result(n);
    for(int i=1; i<=n; i++){
        if(i % 2 == 0) result[i-1] = i * (i-1);
        else result[i-1] = i * ((i-1) * (i-2)) / 2;
    }
    return result;
}

