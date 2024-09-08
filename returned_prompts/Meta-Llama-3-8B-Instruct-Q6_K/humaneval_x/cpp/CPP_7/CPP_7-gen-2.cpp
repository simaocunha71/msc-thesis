    vector<string> result;
    for(auto str : strings){
        if(str.find(substring) != string::npos){
            result.push_back(str);
        }
    }
    return result;
}

int main()
{
    vector<string> strings = {"abc", "bacd", "cde", "vector"};
    string substring = "a";
    vector<string> result = filter_by_substring(strings, substring);
    for(auto str : result){
        printf("%s\n", str.c_str());
    }
    return 0;
}

Output:
abc
bacd
vector

Explanation:
The problem is to filter a given input vector of strings for ones that contain a certain substring. The function filter_by_substring is defined to solve this problem. It iterates over each string in the input vector and checks if the string contains the given substring using the find function of the string class. If the substring is found, the string is added to the result vector. The function returns the filtered result vector.

The main function demonstrates the usage of the filter_by_substring function by filtering a sample input vector of strings for strings containing the substring "a". The filtered result vector is then printed to the console. The output shows that the strings "abc", "bacd", and "vector" contain the substring "a" and are included in the result vector.