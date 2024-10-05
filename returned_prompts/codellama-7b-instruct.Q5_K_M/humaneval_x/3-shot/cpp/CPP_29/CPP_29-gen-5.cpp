    vector<string> result;
    for (auto &s:strings)
    if (s.find(prefix)==0)
    result.push_back(s);
    return result;
}


