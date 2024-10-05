    vector<string> words;
    vector<string> result;
    string word = "";
    for (int i = 0; i < s.length(); i++)
    {
        if (s[i] == ' ')
        {
            words.push_back(word);
            word = "";
        }
        else
        {
            word = word + s[i];
        }
    }
    words.push_back(word);
    for (int i = 0; i < words.size(); i++)
    {
        int count = 0;
        for (int j = 0; j < words[i].length(); j++)
        {
            char c = tolower(words[i][j]);
            if (c != 'a' && c != 'e' && c != 'i' && c != 'o' && c != 'u' && c != ' ')
            {
                count++;
            }
        }
        if (count == n)
        {
            result.push_back(words[i]);
        }
    }
    return result;
}
int main()
{
    vector<string> res = select_words("Mary had a little lamb", 4);
    for(auto i:res)
        printf("%s ", i.c_str());
    printf("\n");
    res = select_words("Mary had a little lamb", 3);
    for(auto i:res)
        printf("%s ", i.c_str());
    printf("\n");
    res = select_words("simple white space", 2);
    for(auto i:res)
        printf("%s ", i.c_str());
    printf("\n");
    res = select_words("Hello world", 4);
    for(auto i:res)
        printf("%s ", i.c_str());
    printf("\n");
    res = select_words("Uncle sam", 3);
    for(auto i:res)
        printf("%s ", i.c_str());
    printf("\n");
    return 0;
}

*/

