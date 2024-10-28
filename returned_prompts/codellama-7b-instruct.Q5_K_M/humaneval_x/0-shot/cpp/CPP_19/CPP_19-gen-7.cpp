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
    map<string,int> number_map;
    int length = numbers.length();
    for(int i=0;i<length;i++){
        int index = i;
        while(index<length && numbers[index]!=32){
            number_map[numbers[index]]++;
            index++;
        }
    }
    string sorted_numbers;
    while(number_map.size()>0){
        string key;
        int min = 10;
        for(map<string,int>::iterator it = number_map.begin();it!=number_map.end();it++){
            if(it->second<min){
                min = it->second;
                key = it->first;
            }
        }
        sorted_numbers+=key;
        number_map.erase(key);
    }
    return sorted_numbers;
}



