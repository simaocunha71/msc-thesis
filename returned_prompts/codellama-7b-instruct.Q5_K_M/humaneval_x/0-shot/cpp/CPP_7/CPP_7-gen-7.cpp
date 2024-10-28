    vector<string> filtered_vector;
    for (int i = 0; i < strings.size(); i++)
    {
        if(strings[i].find(substring) != string::npos)
        {
            filtered_vector.push_back(strings[i]);
        }
    }
    return filtered_vector;
}

