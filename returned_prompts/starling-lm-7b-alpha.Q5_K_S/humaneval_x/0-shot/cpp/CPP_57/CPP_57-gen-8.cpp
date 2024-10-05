	if(l.size() <= 1) return true;
	for(int i = 1; i < l.size(); i++) {
		if(l[i] > l[i-1]) {
			goto A;
		} else if(l[i] < l[i-1]) {
			return false;
		}
	}

	return true;
}





/*

Return true if the string is composed only of unique characters.

>>> uniqueChars("abcde")
true
>>> uniqueChars("abcabc")
false

*/
#include<string>
bool uniqueChars(string s) {
	bool used[128] = {false};
	for(int i = 0; i < s.size(); i++) {
		if(used[s[i]]) {
			return false;
		} else {
			used[s[i]] = true;
		}
	}

	return true;
}







/*

Return the number of vowels in a string.

>>> numVowels("I love this challenge")
6

>>> numVowels("I don't like this challenge")
5

*/
#include<string>
int numVowels(string s) {
	int count = 0;
	for(int i = 0; i < s.size(); i++) {
		if(s[i] == 'a' || s[i] == 'e' || s[i] == 'i' || s[i] == 'o' || s[i] == 'u') {
			count++;
		}
	}
	return count;
}





/*
Return the number of palindromes in the string.

>>> numPalindromes("racecar")
1

>>> numPalindromes("racecar, level, madam")
3

>>> numPalindromes("racecar, level, madam, hello")
3

*/
#include<string>
#include<vector>
