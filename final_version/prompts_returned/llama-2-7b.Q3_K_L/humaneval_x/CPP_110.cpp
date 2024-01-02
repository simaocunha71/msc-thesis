/*
In this problem, you will implement a function that takes two vectors of numbers,
and determines whether it is possible to perform an exchange of elements
between them to make lst1 a vector of only even numbers.
There is no limit on the number of exchanged elements between lst1 and lst2.
If it is possible to exchange elements between the lst1 and lst2 to make
all the elements of lst1 to be even, return "YES".
Otherwise, return "NO".
For example:
exchange({1, 2, 3, 4}, {1, 2, 3, 4}) => "YES"
exchange({1, 2, 3, 4}, {1, 5, 3, 4}) => "NO"
It is assumed that the input vectors will be non-empty.
*/
#include<stdio.h>
#include<vector>
#include<string>
using namespace std;
string exchange(vector<int> lst1,vector<int> lst2){
	if(lst1.size()==0 || lst2.size()==0) return "No"; //empty vectors
	int even= 0;
	//for i in lst1 : even+=i%2;
	//for j in lst2:even+=j%2;
	if(even>0){
	    if((lst1.size()==2 && lst1[0]%2 == lst1[1]) || (lst1.size()==4 && lst1[0]%2 == lst1[3] && lst1[2]%2 == lst1[3])){ //check if it is already even
	        return "YES";
	    }else {
	        swap(lst1,lst2);
	        exchange(lst1,lst2);
	    }
	}
	return "NO" ;//else
}
int main(){
	vector<int> lst1={5,1,7};
	vector<int> lst2={9,3,2};
	string res;
	res=exchange(lst1,lst2);
}