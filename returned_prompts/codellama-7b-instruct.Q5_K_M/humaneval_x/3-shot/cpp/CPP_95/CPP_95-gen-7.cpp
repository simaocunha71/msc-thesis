    if (dict.empty()) return false;
    string key;
    int case_count=0;
    for (auto& x: dict)
    {
        key=x.first;
        if (key==key) case_count+=1;
    }
    if (case_count==dict.size()) return true;
    else return false;
}


