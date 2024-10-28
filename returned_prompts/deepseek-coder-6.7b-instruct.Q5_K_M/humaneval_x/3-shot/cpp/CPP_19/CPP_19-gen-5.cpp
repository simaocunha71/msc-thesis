    map<string, int> dict = { {"zero", 0}, {"one", 1}, {"two", 2}, {"three", 3}, {"four", 4}, {"five", 5}, {"six", 6}, {"seven", 7}, {"eight", 8}, {"nine", 9}};
    vector<string> number_vec;
    string word = "";
    for (int i = 0; i < numbers.size(); i++)
    {
        if (numbers[i] == ' ')
        {
            number_vec.push_back(word);
            word = "";
        }
        else
        {
            word = word + numbers[i];
        }
    }
    number_vec.push_back(word);
    sort(number_vec.begin(), number_vec.end(), [&dict](const string &a, const string &b) {
        return dict[a] < dict[b];
    });
    string sorted_numbers = "";
    for (string number : number_vec)
    {
        sorted_numbers = sorted_numbers + number + " ";
    }
    return sorted_numbers.substr(0, sorted_numbers.size() - 1);
}


