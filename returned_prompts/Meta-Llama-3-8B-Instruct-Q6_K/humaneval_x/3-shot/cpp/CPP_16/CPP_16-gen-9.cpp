    vector<char> char_vector;
    for(int i=0; i<str.length(); i++)
    {
        if(find(char_vector.begin(), char_vector.end(), tolower(str[i])) == char_vector.end())
        {
            char_vector.push_back(tolower(str[i]));
        }
    }
    return char_vector.size();
}
