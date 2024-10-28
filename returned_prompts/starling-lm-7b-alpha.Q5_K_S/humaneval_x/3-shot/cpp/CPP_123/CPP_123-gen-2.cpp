    vector<int> collatz;
    int i,j;
    int current_number;
    int current_collatz;
    int next_collatz;
    for (i=n;i>0;i--)
    {
        current_number=i;
        collatz.clear();
        collatz.push_back(i);
        while (current_number!=1)
        {
            if (current_number%2==1){
                next_collatz=current_number*3+1;
                collatz.push_back(next_collatz);
                current_number=next_collatz;
            }
            if (current_number%2==0){
                next_collatz=current_number/2;
                collatz.push_back(next_collatz);
                current_number=next_collatz;
            }
        }
    }
    sort(collatz.begin(), collatz.end());
    return collatz;
}


