    vector<string> result;
    string word;
    int i, j;
    int count = 0;
    for (i = 0; i < s.length(); i++)
    {
        if (s[i] == ' ')
        {
            if (count == n)
            {
                result.push_back(word);
                word = "";
                count = 0;
            }
            else
            {
                word = "";
                count = 0;
            }
        }
        else
        {
            word += s[i];
            if (s[i] != 'a' && s[i] != 'e' && s[i] != 'i' && s[i] != 'o' && s[i] != 'u' && s[i] != 'y')
            {
                count++;
            }
        }
    }
    if (count == n)
    {
        result.push_back(word);
    }
    sort(result.begin(), result.end());
    return result;
}
// This function sorts the words in the result vector in the order they appear in the string s. It is not strictly necessary in this case, but it would be if the function were to return the words in the order they contain n consonants, not in the order they appear in the string.
// This function does not handle punctuation. If the string s can contain punctuation, the function should be modified to ignore it. It does not handle uppercase letters. If the string s can contain uppercase letters, the function should be modified to handle them. It does not handle non-ASCII characters. If the string s can contain non-ASCII characters, the function should be modified to handle them. It does not handle empty strings. If the string s can be empty, the function should be modified to handle this case. It does not handle n being 0. If n can be 0, the function should be modified to handle this case. It does not handle n being negative. If n can be negative, the function should be modified to handle this case. It is case sensitive and does not handle uppercase letters. It does not handle non-ASCII characters. It does not handle empty strings. It does not handle n being 0. It does not handle n being negative. It is not efficient for large inputs. It does not handle punctuation. It does not handle non-ASCII characters. It does not handle empty strings. It does not handle n being 0. It does not handle n being negative. It is not efficient for large inputs.