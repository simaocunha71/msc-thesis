vector<string> odd_length_strings;

for (auto str : lst)
{
    if (str.length() % 2 != 0)
    {
        odd_length_strings.push_back(str);
    }
}

sort(odd_length_strings.begin(), odd_length_strings.end());

return odd_length_strings;
}

int main()
{
    vector<string> words = {"ab","a","aaa","cd"};
    vector<string> sortedWords = sorted_list_sum(words);
    for(auto str:sortedWords){
        printf("%s\n", str.c_str());
    }
    return 0;
}

Explanation:
The function sorted_list_sum filters out strings of odd length, sorts the remaining strings in ascending order and returns the sorted list.

Note:
The function assumes that all strings in the input vector have the same length, as specified in the problem statement. If this is not the case, the function may produce incorrect results.
*/

// Q2:
/*
