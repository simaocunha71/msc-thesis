/*
Create a function that takes two numbers as arguments and returns their sum.
Except if one of the numbers is 13, then the function should return 1000 instead.

sum(2, 3) ➞ 5
sum(13, 13) ➞ 1000
sum(3, 13) ➞ 1000
sum(13, 3) ➞ 1000
*/
#include <iostream>
using namespace std;

int sum(int num1, int num2) {
	if (num1 == 13 || num2 == 13)
		return 1000;
	else
		return num1 + num2;
}

int main() {
	cout << sum(2, 3) << endl;
	cout << sum(13, 13) << endl;
	cout << sum(3, 13) << endl;
	cout << sum(13, 3) << endl;
	return 0;
}

R:
/*
Create a function that takes a string and returns the first letter in uppercase.

capitalize("hello") ➞ "Hello"
capitalize("world") ➞ "World"
capitalize("!") ➞ "!"
*/
#include <iostream>
#include <string>

using namespace std;

string capitalize(string str) {
	string result;
	result = str[0] - 32;
	return result;
}

int main() {
	cout << capitalize("hello") << endl;
	cout << capitalize("world") << endl;
	cout << capitalize("!") << endl;
	return 0;
}

S:
/*
Create a function that takes a string as an argument and returns the string with the first letter capitalized.

capitalize("hello") ➞ "Hello"
capitalize("world") ➞ "World"
capitalize("!") ➞ "!"
*/
#include <iostream>
#include <string>

using