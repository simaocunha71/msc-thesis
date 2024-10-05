    vector<string> result;
    for(const auto& s : strings){
        if(s.find(substring) != string::npos){
            result.push_back(s);
        }
    }
    return result;
}

int main() {
    vector<string> strings = {"abc", "bacd", "cde", "vector"};
    string substring = "a";
    vector<string> result = filter_by_substring(strings, substring);
    for(const auto& s : result){
        printf("%s\n", s.c_str());
    }
    return 0;
}

*/

//C++/cpp_filter_vector_by_substring.cpp
#include<iostream>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;

vector<string> filter_by_substring(vector<string> strings, string substring){
    vector<string> result;
    copy_if(strings.begin(), strings.end(), back_inserter(result), [&](const string& s){
        return s.find(substring) != string::npos;
    });
    return result;
}

int main() {
    vector<string> strings = {"abc", "bacd", "cde", "vector"};
    string substring = "a";
    vector<string> result = filter_by_substring(strings, substring);
    for(const auto& s : result){
        cout << s << endl;
    }
    return 0;
}

//C++/cpp_find_in_vector.cpp
#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int find_in_vector(vector<int> vec, int num){
    auto it = find(vec.begin(), vec.end(), num);
    if(it != vec.end()){
        return distance(vec.begin(), it);
    }else{
        return -1;
    }
}

int main() {
    vector<int