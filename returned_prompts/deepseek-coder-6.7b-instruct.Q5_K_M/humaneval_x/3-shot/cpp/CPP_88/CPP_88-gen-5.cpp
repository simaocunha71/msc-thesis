    vector<int> sorted_array(array);

    if((sorted_array.front() + sorted_array.back()) % 2 == 0)
        sort(sorted_array.begin(), sorted_array.end(), greater<int>());
    else
        sort(sorted_array.begin(), sorted_array.end());

    return sorted_array;
}


