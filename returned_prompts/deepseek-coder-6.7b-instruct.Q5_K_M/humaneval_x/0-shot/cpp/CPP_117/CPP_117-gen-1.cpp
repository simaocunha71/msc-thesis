vector<string> words;
vector<string> result;
string word = "";
for (int i = 0; i < s.length(); i++)
{
    if (s[i] != ' ')
        word += s[i];
    else
    {
        words.push_back(word);
        word = "";
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
            count++;
    }
    if (count == n)
        result.push_back(words[i]);
}
return result;
}

//Test the function
int main() {
    vector<string> words = select_words("Mary had a little lamb", 4);
    for(int i = 0; i < words.size(); i++)
        printf("%s ", words[i].c_str());
    printf("\n");
    return 0;
}


*/

//C++ program to implement a function to count the number of words in a string that contain exactly n vowels

/*
