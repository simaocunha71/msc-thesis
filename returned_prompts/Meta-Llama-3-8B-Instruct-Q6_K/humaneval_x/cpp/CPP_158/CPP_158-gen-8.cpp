    // Initialize variables
    int max_count = 0;
    string result = "";

    // Iterate over each word in the vector
    for (const string& word : words) {
        // Count the number of unique characters in the word
        set<char> unique_chars(word.begin(), word.end());
        int count = unique_chars.size();

        // If the word has more unique characters than the current max, update the max and result
        if (count > max_count) {
            max_count = count;
            result = word;
        }
        // If the word has the same number of unique characters as the current max, and it comes first in lexicographical order, update the result
        else if (count == max_count) {
            if (word < result) {
                result = word;
            }
        }
    }

    // Return the word with the maximum number of unique characters
    return result;
}

