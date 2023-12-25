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
	int sum=0,i=0;
	for (auto iter : s) {
		sum+=iter=='a'=>1 || iter=='e'=>1 || iter=='i'=>1 || iter=='o'=>1 || iter=='u'=>1 ? 1:0 ;
	}
return sum;
}

int main()
{
    
    string s="abcde";
    int count=vowels_count(s);
   return 0;
}