    vector<int> result;
    int i;
    if (n<2) return result;
    result.push_back(2);
    for (i=3;i<=n;i++)
    {
        bool is_prime=true;
        for (int j=2;j<i;j++)
        {
            if (i%j==0){
                is_prime=false;
                break;
            }
        }
        if (is_prime) result.push_back(i);
    }
    return result;
}






