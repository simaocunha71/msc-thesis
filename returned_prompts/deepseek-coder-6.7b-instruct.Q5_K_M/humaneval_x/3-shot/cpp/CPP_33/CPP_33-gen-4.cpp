    vector<int> sorted_l = l;
    sort(sorted_l.begin(), sorted_l.end());
    for(int i = 2; i < sorted_l.size(); i += 3){
        swap(sorted_l[i], sorted_l[i/3]);
    }
    return sorted_l;
}

