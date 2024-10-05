    vector<float> even_indicies;
    for (int i = 0; i < l.size(); i += 2)
        even_indicies.push_back(l[i]);

    sort(even_indicies.begin(), even_indicies.end());

    for (int i = 0, j = 0; i < l.size(); i += 2, ++j)
        l[i] = even_indicies[j];

    return l;
}


