    vector<int> new_vector;
    new_vector.push_back(numbers[0]);
    for (int i=1;i<numbers.size();i++)
    new_vector.push_back(delimeter);
    for (int i=1;i<numbers.size();i++)
    new_vector.push_back(numbers[i]);
    return new_vector;
}



