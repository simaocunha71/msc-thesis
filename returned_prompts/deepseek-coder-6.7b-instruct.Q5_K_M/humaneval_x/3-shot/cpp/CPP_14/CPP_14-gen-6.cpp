    vector<string> result;
    for (size_t i = 0; i < str.size(); ++i)
        result.push_back(str.substr(0, i + 1));
    return result;
}


