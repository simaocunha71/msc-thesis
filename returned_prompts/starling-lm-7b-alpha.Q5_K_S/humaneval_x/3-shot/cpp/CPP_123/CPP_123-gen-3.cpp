    vector<int> collatz_odd;
    int i,next_number;
    for (i=n;i>0;i--)
    {
        if (i%2==1){
        next_number=i*3+1;
        collatz_odd.push_back(next_number);
        }
    }
    sort(collatz_odd.begin(),collatz_odd.end());
    return collatz_odd;
}



