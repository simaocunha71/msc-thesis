    vector<char> char_vector;
    for (int i=0; i<str.length(); i++)
    {
        char_vector.push_back(tolower(str[i]));
    }
    sort(char_vector.begin(), char_vector.end());
    int count = 1;
    for (int i=1; i<char_vector.size(); i++)
    {
        if (char_vector[i] != char_vector[i-1])
        {
            count++;
        }
    }
    return count;
}
// Alternate solution using set
int count_distinct_characters(string str){ 
    set<char> char_set;
    for (int i=0; i<str.length(); i++)
    {
        char_set.insert(tolower(str[i]));
    }
    return char_set.size();
} 





