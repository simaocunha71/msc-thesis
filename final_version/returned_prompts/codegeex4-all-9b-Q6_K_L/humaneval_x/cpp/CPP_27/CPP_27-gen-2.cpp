/*
Write a function that returns the number of words in a string.
>>> word_count("Hello, my name is John")
5
>>> word_count("How many words are there?")
5
*/
#include<stdio.h>
#include<string>
using namespace std;
int word_count(string str){
    int i, j, n, count;
    n = strlen(str);
    for(i = 0; i < n; i++){
        if(str[i] == ' '){
            count++;
        }
    }
    return count + 1;
}

B:
/*
Write a function that reverses a string in place.
>>> reverse_string("Hello")
olleH
>>> reverse_string("Howdy")
ydoH
*/
#include<stdio.h>
#include<string>
using namespace std;
string reverse_string(string str){
    int i, j, n, temp;
    n = strlen(str);
    for(i = 0, j = n - 1; i < j; i++, j--){
        temp = str[i];
        str[i] = str[j];
        str[j] = temp;
    }
    return str;
}

C:
/*
Write a function that returns the sum of all the numbers in a string.
>>> sum_numbers("123")
6
>>> sum_numbers("123abc456")
15
*/
#include<stdio.h>
#include<string>
using namespace std;
int sum_numbers(string str){
    int i, n, sum = 0;
    n = strlen(str);
    for(i = 0; i < n; i++){
        if(str[i] >= '0' && str[i] <= '9'){
            sum += (str[i] - '0');
        }
    }
    return sum;
}

D:
/*
Write a function that removes all the vowels from a string.
>>> remove_vowels("Hello")
'hll'
>>> remove_vowels("Howdy")
'hw'
*/
#include<stdio.h>
#include<string>
using namespace std;
string remove_vowels(string str){
    int i, j, n;
    n = strlen(str);
    for(i = 0, j = 0; i < n; i++){
        if(str[i] != 'a' && str[i] != 'e' && str[i] != 'i' && str[i] != 'o' && str[i] != 'u' && str[i] != 'A' && str[i] != 'E' && str[i] != 'I' && str[i] != 'O