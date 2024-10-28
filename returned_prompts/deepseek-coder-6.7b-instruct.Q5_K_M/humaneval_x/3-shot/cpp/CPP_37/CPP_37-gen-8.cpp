    vector<float> even_index_elements;
    for (int i=0; i<l.size(); i+=2)
        even_index_elements.push_back(l[i]);

    sort(even_index_elements.begin(), even_index_elements.end());

    for (int i=0, j=0; i<l.size(); i+=2, ++j)
        l[i] = even_index_elements[j];

    return l;
}


