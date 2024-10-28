    vector<string> result;
    for(string s : strings){
        if(s.substr(0, prefix.size()) == prefix){
            result.push_back(s);
        }
    }
    return result;
}
int main(){
    vector<string> strings = {"abc", "bcd", "cde", "vector"};
    string prefix = "a";
    vector<string> result = filter_by_prefix(strings, prefix);
    for(string s : result){
        printf("%s\n", s.c_str());
    }
    return 0;
}

*/

// C++ Solution
#include <iostream>
#include <vector>
#include <string>
using namespace std;

vector<string> filter_by_prefix(vector<string> strings, string prefix){
    vector<string> result;
    for(string s : strings){
        if(s.substr(0, prefix.size()) == prefix){
            result.push_back(s);
        }
    }
    return result;
}

int main(){
    vector<string> strings = {"abc", "bcd", "cde", "vector"};
    string prefix = "a";
    vector<string> result = filter_by_prefix(strings, prefix);
    for(string s : result){
        cout << s << endl;
    }
    return 0;
}
/*
abc
vector
*/


*/

// C# Solution
using System;
using System.Collections.Generic;

public class Program
{
    public static List<string> FilterByPrefix(List<string> strings, string prefix)
    {
        List<string> result = new List<string>();
        foreach (string s in strings)
        {
            if (s.StartsWith(prefix))
            {
                result.Add(s);
            }
        }
        return result;
    }

    public static void Main()
    {
        List<string> strings = new List<string>{"abc", "bcd", "cde", "vector"};
        string prefix = "a