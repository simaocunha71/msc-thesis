    map<string, int> word_to_num = {{"zero", 0}, {"one", 1}, {"two", 2}, {"three", 3}, {"four", 4},
 {"five", 5}, {"six", 6}, {"seven", 7}, {"eight", 8}, {"nine", 9}};
    map<int, string> num_to_word = {{0, "zero"}, {1, "one"}, {2, "two"}, {3, "three"}, {4, "four"},
 {5, "five"}, {6, "six"}, {7, "seven"}, {8, "eight"}, {9, "nine"}};

    string word = "";
    string number_string = "";
    vector<string> number_words;
    for(char c : numbers){
        if (c == ' '){
            number_words.push_back(word);
            word = "";
        } else {
            word += c;
        }
    }
    number_words.push_back(word);
    sort(number_words.begin(), number_words.end(), [&](const string &a, const string &b){
        return word_to_num[a] < word_to_num[b];
    });
    for(string num_word : number_words){
        number_string += num_to_word[word_to_num[num_word]] + " ";
    }
    number_string.pop_back();
    return number_string;
}


