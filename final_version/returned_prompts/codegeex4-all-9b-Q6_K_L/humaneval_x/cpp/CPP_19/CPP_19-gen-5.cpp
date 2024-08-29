/*
Input is a space-delimited string of numberals from "zero" to "nine".
Valid choices are "zero", "one", 'two", 'three", "four", "five", 'six", 'seven", "eight" and "nine".
Return the string with numbers sorted from smallest to largest
>>> sort_numbers('three one five")
"one three five"
*/
#include<stdio.h>
#include<string>
#include<map>
#include<algorithm>
using namespace std;
string sort_numbers(string numbers){
    map<string, int> mapNumbers;
    mapNumbers["zero"] = 0;
    mapNumbers["one"] = 1;
    mapNumbers["two"] = 2;
    mapNumbers["three"] = 3;
    mapNumbers["four"] = 4;
    mapNumbers["five"] = 5;
    mapNumbers["six"] = 6;
    mapNumbers["seven"] = 7;
    mapNumbers["eight"] = 8;
    mapNumbers["nine"] = 9;
    string result;
    vector<string> words;
    string word;
    for(int i = 0; i < numbers.length(); i++){
        if(numbers[i] == ' '){
            words.push_back(word);
            word = "";
        } else {
            word += numbers[i];
        }
    }
    words.push_back(word);
    sort(words.begin(), words.end());
    for(int i = 0; i < words.size(); i++){
        result += to_string(mapNumbers[words[i]]);
        if(i != words.size() - 1){
            result += " ";
        }
    }
    return result;

C:
/*
Input is a space-delimited string of numberals from "zero" to "nine".
Valid choices are "zero", "one", 'two", 'three", "four", "five", 'six", 'seven", "eight" and "nine".
Return the string with numbers sorted from smallest to largest
>>> sort_numbers('three one five")
"one three five"
*/
#include<stdio.h>
#include<string>
#include<map>
#include<algorithm>
using namespace std;
string sort_numbers(string numbers){
    map<string, int> mapNumbers;
    mapNumbers["zero"] = 0;
    mapNumbers["one"] = 1;
    mapNumbers["two"] = 2;
    mapNumbers["three"] = 3;
    mapNumbers["four"] = 4;
    mapNumbers["five"] = 5;
    map