    map<string, int> words_to_nums = {{"zero", 0}, {"one", 1}, {"two", 2}, {"three", 3}, {"four", 4},
 {"five", 5}, {"six", 6}, {"seven", 7}, {"eight", 8}, {"nine", 9}};
    map<int, string> nums_to_words = {{0, "zero"}, {1, "one"}, {2, "two"}, {3, "three"}, {4, "four"},
 {5, "five"}, {6, "six"}, {7, "seven"}, {8, "eight"}, {9, "nine"}};

    vector<string> num_words;
    string word = "";
    for (char &c : numbers)
    {
        if (c == ' ')
        {
            num_words.push_back(word);
            word = "";
        }
        else
        {
            word += c;
        }
    }
    num_words.push_back(word);
    sort(num_words.begin(), num_words.end(), [&](string a, string b){ return words_to_nums[a] < words_to_nums[b]; });
    string sorted_nums = "";
    for (string num_word : num_words)
    {
        sorted_nums += num_to_words[words_to_nums[num_word]] + " ";
    }
    return sorted_nums.substr(0, sorted_nums.size()-1);
}


