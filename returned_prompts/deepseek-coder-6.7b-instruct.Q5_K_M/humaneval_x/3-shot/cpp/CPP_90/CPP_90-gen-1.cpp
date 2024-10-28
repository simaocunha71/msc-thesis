    int first_min = INT_MAX, second_min = INT_MAX;
    for(int i = 0; i < lst.size(); i++){
        if (lst[i] < first_min) {
            second_min = first_min;
            first_min = lst[i];
        } else if (lst[i] < second_min && lst[i] != first_min) {
            second_min = lst[i];
        }
    }
    if (second_min == INT_MAX) 
        return None;
    else
        return second_min;
}


