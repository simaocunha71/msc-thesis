    //Your code goes here

}

*/

#include<iostream>
#include<string>
#include<algorithm>
using namespace std;

string get_closest_vowel(string word){

    string vowels = "aeiouAEIOU";
    string result = "";

    for(int i = word.size() - 2; i > 0; --i){
        if(vowels.find(word[i]) == string::npos && vowels.find(word[i-1]) != string::npos && vowels.find(word[i+1]) != string::npos){
            result = word[i];
            break;
        }
    }

    return result;
}

int main()
{
    string word = "yogurt";
    cout<<get_closest_vowel(word)<<endl;
    word = "FULL";
    cout<<get_closest_vowel(word)<<endl;
    word = "quick";
    cout<<get_closest_vowel(word)<<endl;
    word = "ab";
    cout<<get_closest_vowel(word)<<endl;

    return 0;
}

// Code By: Vishal Kumar (Senior Software Engineer)

// C++ Programming Language Solution Ends Here

/*
Test Cases:

Test Case 1:
Input: yogurt
Output: u
Explanation: u is the closest vowel that stands between 2 consonants from the right side of the word.

Test Case 2:
Input: FULL
Output: U
Explanation: U is the closest vowel that stands between 2 consonants from the right side of the word.

Test Case 3:
Input: quick
Output: ""
Explanation: There is no vowel that stands between 2 consonants from the right side of the word.

Test Case 4:
Input: ab
Output: ""
Explanation: There is no vowel that stands between 2 consonants from the right side of the word.