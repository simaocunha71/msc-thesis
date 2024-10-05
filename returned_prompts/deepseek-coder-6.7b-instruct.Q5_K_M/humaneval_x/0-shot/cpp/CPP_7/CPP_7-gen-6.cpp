vector<string> result;

for (const auto& str : strings) {
    if (str.find(substring) != string::npos) {
        result.push_back(str);
    }
}

return result;
}

int main(){
vector<string> strings = {"abc", "bacd", "cde", "vector"};
string substring = "a";
vector<string> filtered = filter_by_substring(strings, substring);
for (const auto& str : filtered) {
    printf("%s\n", str.c_str());
}
return 0;
}
*/


