/*
Write a function vowels_count which takes a string representing a word as input and returns the number of vowels in the string. Vowels in this case are 'a', 'e', 'i', 'o', 'u'. 
Here, 'y' is also a vowel, but only when it is at the end of the given word.
Example: 
>>> vowels_count("abcde") 
2 
>>> vowels_count("ACEDY") 
3
*/
#include<stdio.h>
#include<string>
#include<algorithm>
using namespace std;
int vowels_count(string s){

    int count = 0;
    for(int i = 0; i < s.length(); i++){
        if(s[i] == 'a' || s[i] == 'e' || s[i] == 'i' || s[i] == 'o' || s[i] == 'u'){
            count++;
        }
        if(s[i] == 'y' && i == s.length() - 1) count++;
    }
    return count;
}

// Test case 1:
    int test = vowels_count("abcde");
    assert(test == 2);
// Test case 2:
    int test = vowels_count("ACEDY");
    assert(test == 3);
// Test case 3:
    int test = vowels_count("aeiouy");
    assert(test == 6);
// Test case 4:
    int test = vowels_count("AEIOUY");
    assert(test == 6);
// Test case 5:
    int test = vowels_count("");
    assert(test == 0);


