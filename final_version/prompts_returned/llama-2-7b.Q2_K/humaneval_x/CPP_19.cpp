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
	int min=0,max=9,i=1;  //max is the highest number in nums and i is our current position to find max..
	while(i<=max){
		if(numbers[i]>max)min=i;
	}
	map<string,int> m;
	for(int j=0;j<min+1;++j)m[numbers[j]]++;
	string nums;
	for(auto it=m.begin();it!=m.end();++it){
		nums+=to_string(*it);
	}
	return nums;
}

int main(){
	sort_numbers("one two three four five six seven eight nine");
	return 0;
}
