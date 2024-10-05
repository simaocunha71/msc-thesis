    vector<int> odd_collatz;
    int num=n;
    while(num!=1){
        if(num%2==0) num=num/2;
        else num=num*3+1;
        if(num%2!=0) odd_collatz.push_back(num);
    }
    sort(odd_collatz.begin(), odd_collatz.end());
    return odd_collatz;
}