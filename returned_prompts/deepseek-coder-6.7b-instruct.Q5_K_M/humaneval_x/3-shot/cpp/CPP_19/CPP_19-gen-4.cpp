    map<string, int> nums={{"zero",0}, {"one",1}, {"two",2}, {"three",3}, {"four",4}, {"five",5}, {"six",6}, {"seven",7}, {"eight",8}, {"nine",9}};
    stringstream ss(numbers);
    string word;
    vector<string> words;
    while(ss >> word)
    {
        words.push_back(word);
    }
    sort(words.begin(), words.end(), [&nums](const string &a, const string &b)
    {
        return nums[a] < nums[b];
    });

    ostringstream oss;
    copy(words.begin(), words.end() - 1, ostream_iterator<string>(oss, " "));
    oss << words.back(); // to avoid space at the end
    return oss.str();
}

