    vector<string> names = {"One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"};
    map<int, string> num_to_name;
    for (int i = 1; i <= 9; i++)
        num_to_name[i] = names[i-1];

    vector<int> filtered;
    for (int num : arr)
        if (num_to_name.count(num) > 0)
            filtered.push_back(num);

    sort(filtered.begin(), filtered.end());
    reverse(filtered.begin(), filtered.end());

    vector<string> result;
    for (int num : filtered)
        result.push_back(num_to_name[num]);

    return result;
}


