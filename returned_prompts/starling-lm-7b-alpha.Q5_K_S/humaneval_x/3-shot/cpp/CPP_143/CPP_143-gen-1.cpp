    int i,j;
    vector<int> all_primes;
    string res="";
    char chr;
    bool is_prime;
    for (i=2;i<=100;i++)
    {
        is_prime=true;
        for (j=2;j<i;j++)
        if (i%j==0){
        is_prime=false;
        break;
        }
        if (is_prime)
        all_primes.push_back(i);
    }

    chr=sentence[0];
    for (i=1;i<sentence.length();i++)
    {
        chr=sentence[i];
        if (find(all_primes.begin(),all_primes.end(),chr-'a')!=all_primes.end())
        res+=chr;
    }
    return res;
}




