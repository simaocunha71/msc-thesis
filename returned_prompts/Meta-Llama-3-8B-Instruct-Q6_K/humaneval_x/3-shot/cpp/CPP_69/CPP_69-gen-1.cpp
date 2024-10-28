    map<int, int> frequency;
    for (int i : lst) {
        if (frequency.find(i) == frequency.end())
            frequency[i] = 1;
        else
            frequency[i]++;
    }
    for (auto it = frequency.begin(); it != frequency.end(); it++) {
        if (it->second >= it->first) {
            return it->first;
        }
    }
    return -1;
}

