    map<string, int> word_to_num = { {"zero", 0}, {"one", 1}, {"two", 2}, {"three", 3}, {"four", 4},
                              {"five", 5}, {"six", 6}, {"seven", 7}, {"eight", 8}, {"nine", 9} };
    map<int, string> num_to_word = { {0, "zero"}, {1, "one"}, {2, "two"}, {3, "three"}, {4, "four"},
                              {5, "five"}, {6, "six"}, {7, "seven"}, {8, "eight"}, {9, "nine"} };

    string result;
    string word;
    vector<int> nums;

    istringstream iss(numbers);
    while(iss >> word){
        nums.push_back(word_to_num[word]);
    }

    sort(nums.begin(), nums.end());

    for(int num : nums){
        result += num_to_word[num] + " ";
    }

    return result.substr(0, result.length()-1); // remove the trailing space
}


