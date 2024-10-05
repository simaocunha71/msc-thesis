    vector<string> result;
    for(int i = 0; i < strings.size(); i++){
        if(strings[i].substr(0, prefix.length()) == prefix){
            result.push_back(strings[i]);
        }
    }
    return result;
}

int main(){
    vector<string> strings = {"abc", "bcd", "cde", "vector"};
    string prefix = "a";
    vector<string> result = filter_by_prefix(strings, prefix);
    for(int i = 0; i < result.size(); i++){
        printf("%s\n", result[i].c_str());
    }
    return 0;
}


A: The code you've written seems fine for your task. It loops through the vector of strings and checks each string against the prefix, if it starts with the prefix, it adds it to the result vector.
The code then prints out the elements of the result vector.
Remember to include the appropriate libraries at the top of your code:
#include <iostream>
#include <vector>
#include <string>

And to use std namespace:
using namespace std;


A: Your code is correct. Here is a slight modification to make it more generic.
#include <iostream>
#include <vector>
#include <string>

std::vector<std::string> filter_by_prefix(const std::vector<std::string>& strings, const std::string& prefix){
    std::vector<std::string> result;
    for(const auto& str : strings){
        if(str.substr(0, prefix.length()) == prefix){
            result.push_back(str);
        }
    }
    return result;
}

int main(){
    std::vector<std::string> strings = {"abc", "bcd", "cde", "vector"};
    std::string prefix = "a";
    std::vector<std::string> result = filter_by_prefix(strings, prefix);
    for(const auto& str : result){
        std::cout << str << std::endl;
    }
    return 