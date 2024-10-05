    vector<int> tri_numbers;
    int current_number=1;
    int next_number=3;
    int next_next_number=1;
    int i;
    tri_numbers.push_back(current_number);
    tri_numbers.push_back(next_number);
    tri_numbers.push_back(next_next_number);
    for (i=3;i<=n;i++){
        current_number=next_number;
        next_number=next_next_number;
        if (i%2==0)
        next_next_number=current_number+next_number;
        else
        next_next_number=next_number+current_number+next_next_number;
        tri_numbers.push_back(next_next_number);
    }
    return tri_numbers;
}


