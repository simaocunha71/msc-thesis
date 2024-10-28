    vector<string> result;
    for (string word : lst)
    {
        if (word.length() % 2 == 0)
        {
            result.push_back(word);
        }
    }
    sort(result.begin(), result.end());
    return result;
}


