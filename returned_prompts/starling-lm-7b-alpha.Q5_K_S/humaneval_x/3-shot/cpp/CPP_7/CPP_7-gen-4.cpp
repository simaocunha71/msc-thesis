    vector<string> result;
    for (auto str:strings)
    if (str.find(substring)!=string::npos)
    result.push_back(str);

    return result;
}



