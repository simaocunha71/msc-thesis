    vector<string> result;
    map<int, string> number_names = {{1, "One"}, {2, "Two"}, {3, "Three"}, {4, "Four"}, {5, "Five"}, {6, "Six"}, {7, "Seven"}, {8, "Eight"}, {9, "Nine"}};
    vector<int> numbers;
    for (int i=0;i<arr.size();i++)
    {
        if (arr[i]>=1 && arr[i]<=9)
        {
            numbers.push_back(arr[i]);
        }
    }
    sort(numbers.begin(), numbers.end());
    reverse(numbers.begin(), numbers.end());
    for (int i=0;i<numbers.size();i++)
    {
        result.push_back(number_names[numbers[i]]);
    }
    return result;
}