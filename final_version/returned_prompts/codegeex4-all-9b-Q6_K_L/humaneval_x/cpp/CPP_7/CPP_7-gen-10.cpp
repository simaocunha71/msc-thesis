#include <string>
#include <vector>

using namespace std;

vector<string> filter_by_substring(vector<string> strings, string substring)
{
    vector<string> result;
    for (auto s : strings)
    {
        if (s.find(substring) != string::npos)
        {
            result.push_back(s);
        }
    }
    return result;
}

int main()
{
    vector<string> strings = {"abc", "bacd", "cde", "vector"};
    string substring = "a";
    vector<string> result = filter_by_substring(strings, substring);
    for (auto s : result)
    {
        printf("%s\n", s.c_str());
    }
    return 0;
}

