    vector<int> levels;
    int i,next_level;
    for (i=1;i<=n;i++)
    {
        next_level=i+2*(i%2);
        levels.push_back(next_level);
    }
    return levels;
}


