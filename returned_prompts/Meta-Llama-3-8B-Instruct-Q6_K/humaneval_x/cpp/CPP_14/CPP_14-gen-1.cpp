    vector<string> prefixes;
    for(int i = 1; i <= str.length(); i++){
        prefixes.push_back(str.substr(0, i));
    }
    return prefixes;
} // End of all_prefixes function

int main()
{
    string str = "abc";
    vector<string> result = all_prefixes(str);

    for(int i = 0; i < result.size(); i++){
        cout << result[i] << endl;
    }

    return 0;
}

Output:
a
ab
abc

The function all_prefixes() takes a string as input and returns a vector of strings, where each string is a prefix of the input string. The function iterates from 1 to the length of the input string, and for each iteration, it adds a substring of the input string from the beginning to the current iteration number to the vector of prefixes. The function then returns the vector of prefixes. The main function calls the all_prefixes() function with the input string "abc" and prints the resulting vector of prefixes.

Time Complexity: O(n), where n is the length of the input string.
Space Complexity: O(n), where n is the length of the input string. This is because the function creates a vector of strings, where each string is a prefix of the input string, and the size of the vector is equal to the length of the input string.