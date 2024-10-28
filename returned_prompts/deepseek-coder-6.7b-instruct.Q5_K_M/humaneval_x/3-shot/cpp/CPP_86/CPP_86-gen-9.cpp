    string word = "";
    string sorted_word = "";
    for (char &c : s)
    {
        if (c != ' ')
            word += c;
        else
        {
            sort(word.begin(), word.end());
            sorted_word += word + ' ';
            word = "";
        }
    }
    sort(word.begin(), word.end());
    sorted_word += word;
    return sorted_word;
}


