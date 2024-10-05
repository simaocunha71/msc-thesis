    vector<int> levels;
    int current_level=n;
    while (current_level>0)
    {
        levels.push_back(current_level);
        current_level=current_level%2==0?current_level+1:current_level+2;
    }
    return levels;
}


