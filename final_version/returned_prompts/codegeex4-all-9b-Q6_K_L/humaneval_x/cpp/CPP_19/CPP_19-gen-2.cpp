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
using namespace std;
string sort_numbers(string numbers){

    map<string, int> number_map;
    number_map["zero"] = 0;
    number_map["one"] = 1;
    number_map["two"] = 2;
    number_map["three"] = 3;
    number_map["four"] = 4;
    number_map["five"] = 5;
    number_map["six"] = 6;
    number_map["seven"] = 7;
    number_map["eight"] = 8;
    number_map["nine"] = 9;

    vector<int> numbers_vector;
    string number;
    for (int i = 0; i < numbers.length(); i++) {
        if (numbers[i] == ' ') {
            numbers_vector.push_back(number_map[number]);
            number = "";
        } else {
            number += numbers[i];
        }
    }

    sort(numbers_vector.begin(), numbers_vector.end());

    string sorted_numbers = "";
    for (int i = 0; i < numbers_vector.size(); i++) {
        sorted_numbers += number_map[numbers_vector[i]] + " ";
    }

    return sorted_numbers;
}
```c
#include <stdio.h>
#include <string>
#include <map>
using namespace std;

string sort_numbers(string numbers) {
    map<string, int> number_map;
    number_map["zero"] = 0;
    number_map["one"] = 1;
    number_map["two"] = 2;
    number_map["three"] = 3;
    number_map["four"] = 4;
    number_map["five"] = 5;
    number_map["six"] = 6;
    number_map["seven"] = 7;
    number_map["eight"] = 8;
    number_map["nine"] = 9;

    vector<int> numbers_vector;
    string number;
    for (int i = 0; i < numbers.length(); i++) {
        if (numbers[i] == ' ') {
            numbers_vector.push_back(number_map[number]);
