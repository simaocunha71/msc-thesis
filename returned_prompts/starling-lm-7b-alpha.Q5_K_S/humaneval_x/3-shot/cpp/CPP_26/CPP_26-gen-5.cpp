    vector<int> no_dups;
    int i;
    for (i=0;i<numbers.size();i++)
    if (find(no_dups.begin(),no_dups.end(),numbers[i])==no_dups.end())
    no_dups.push_back(numbers[i]);

    return no_dups;
}


