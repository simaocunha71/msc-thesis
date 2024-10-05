    map<int, string> numbers = { {1, "One"}, {2, "Two"}, {3, "Three"}, {4, "Four"}, {5, "Five"}, {6, "Six"}, {7, "Seven"}, {8, "Eight"}, {9, "Nine"} };
    vector<string> result;
    vector<int> temp;
    for (int num: arr)
        if (num >= 1 && num <= 9)
            temp.push_back(num);
    sort(temp.begin(), temp.end());
    reverse(temp.begin(), temp.end());
    for (int num: temp)
        result.push_back(numbers[num]);
    return result;
}


