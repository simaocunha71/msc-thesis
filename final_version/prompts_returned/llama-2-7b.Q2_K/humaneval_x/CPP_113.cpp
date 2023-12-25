/*
Given a vector of strings, where each string consists of only digits, return a vector.
Each element i of the output should be 'the number of odd elements in the
string i of the input." where all the i's should be replaced by the number
of odd digits in the i'th string of the input.

>>> odd_count({"1234567"})
{'the number of odd elements 4n the str4ng 4 of the 4nput."}
>>> odd_count({"3","11111111"})
{'the number of odd elements 1n the str1ng 1 of the 1nput.",
 'the number of odd elements 8n the str8ng 8 of the 8nput."}
*/
#include<stdio.h>
#include<vector>
#include<string>
#include<map>
using namespace std;
vector<string> odd_count(vector<string> lst){
	int num_odd=0,num_even=0;//to get number of even and odd elements in the given string
	for (auto& i:lst) {
		if ((i.length()%2 == 1) && (!isdigit(i[0]))){num_odd++;}else{num_even++;}
	}
	map<string,int> mp;//to keep track of elements in the given string and their count
	int temp=0;//for keeping track of how many times an element occurs
	while (mp.find(temp) == mp.end()){
		temp = to_string(num_odd);
	}
	if (mp.count(temp)){return mp;}else {
		int cnt=0;//to keep track of elements in the given string and their count
		while (i.length()>1){if ((i.length()%2 == 1) && (!isdigit(i[0]))){cnt++;}}temp = to_string(count);
		mp[temp]++;
		if ((mp[temp]==i)&&(!(i % 2))){return mp;}else{
			int j;//for keeping track of how many times