    vector<string> filtered_strings;
    for(auto str:strings){
        if(str.find(substring) != string::npos){
            filtered_strings.push_back(str);
        }
    }
    return filtered_strings;
}

int main(){
    vector<string> strings = {"abc", "bacd", "cde", "vector"};
    vector<string> filtered_strings = filter_by_substring(strings, "a");
    for(auto str:filtered_strings){
        printf("%s\n", str.c_str());
    }
    return 0;
}

The given C++ program filters the input vector of strings to contain only those strings that contain a specific substring. It uses the find method of string class to find the substring in each string of the vector. If the substring is found, the string is added to the output vector.

The filter_by_substring function takes a vector of strings and a substring as arguments and returns a vector of strings that contain the given substring.

The main function demonstrates the usage of the filter_by_substring function by filtering the vector of strings {"abc", "bacd", "cde", "vector"} for the substring "a", and prints the filtered strings to the console.
*/

