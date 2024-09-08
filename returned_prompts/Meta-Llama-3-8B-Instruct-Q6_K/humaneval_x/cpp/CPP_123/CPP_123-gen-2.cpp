    vector<int> res;
    while(n != 1){
        if(n % 2 == 0){
            n = n / 2;
        }
        else{
            n = 3 * n + 1;
        }
        if(n % 2 != 0){
            res.push_back(n);
        }
    }
    res.push_back(1);
    sort(res.begin(), res.end());
    return res;
}

int main()
{
    int n = 5;
    vector<int> res = get_odd_collatz(n);
    for(int i = 0; i < res.size(); i++)
        printf("%d ", res[i]);
    return 0;
}

