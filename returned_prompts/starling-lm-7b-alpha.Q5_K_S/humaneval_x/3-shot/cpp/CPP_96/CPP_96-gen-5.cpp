    vector<int> result;
    int i;
    for (i=2;i<n;i++)
    if (is_prime(i))
    result.push_back(i);

    return result;
}

bool is_prime(int number){
    int i;
    for (i=2;i<number;i++)
    if (number%i==0)
    return false;

    return true;
}



