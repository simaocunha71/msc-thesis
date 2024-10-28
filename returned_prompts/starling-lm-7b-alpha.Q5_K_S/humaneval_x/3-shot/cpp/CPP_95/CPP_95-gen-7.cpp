    for (auto it : dict)
    if (it.first[0]>='a' && it.first[0]<='z')
    if (it.first[0]!=it.second[0])
    return false;

    if (dict.size()==0) return true;

    for (auto it : dict)
    if (it.first[0]>='A' && it.first[0]<='Z')
    if (it.first[0]!=it.second[0])
    return false;

    return true;
}



