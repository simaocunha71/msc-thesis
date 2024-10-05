    vector<string> result;
    for(string s: strings)
        if (s.find(substring) != std::string::npos)
            result.push_back(s);

    return result;
}


