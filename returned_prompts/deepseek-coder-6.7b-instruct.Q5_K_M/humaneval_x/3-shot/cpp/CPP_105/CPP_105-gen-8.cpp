    vector<string> result;
    map<int, string> num_to_name = {{1, "One"}, {2, "Two"}, {3, "Three"}, {4, "Four"}, {5, "Five"}, {6, "Six"}, {7, "Seven"}, {8, "Eight"}, {9, "Nine"}};
    for(int i = 0; i < arr.size(); i++)
    {
        if(arr[i] >= 1 && arr[i] <= 9)
            result.push_back(num_to_name[arr[i]]);
    }
    sort(result.begin(), result.end(), greater<string>());
    return result;
}


