    map<char, int> freq;
    for (char c : test) {
        if (isalpha(c))
            freq[c]++;
    }

    int max_freq = 0;
    for (auto& kv : freq)
        if (kv.second > max_freq)
            max_freq = kv.second;

    map<char, int> result;
    for (auto& kv : freq)
        if (kv.second == max_freq)
            result[kv.first] = kv.second;

    return result;
}


