    vector<int> pile;
    int current_stones=n;
    int level=1;
    int next_stones;
    while (current_stones>0)
    {
        pile.push_back(current_stones);
        if (n%2==0)
        {
            next_stones=current_stones+2;
        }
        else{
            next_stones=current_stones+2;
        }
        level+=1;
        current_stones=next_stones;
    }
    return pile;
}

