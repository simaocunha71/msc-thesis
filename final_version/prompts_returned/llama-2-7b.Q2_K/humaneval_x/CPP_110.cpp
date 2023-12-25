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
	if(!lst1.size() || !lst2.size()) return "N/A"; 
	for(int i=0 ;i<lst1.size(); ++i) if((!lst1[i]%2) && (!lst2[i]%2)) return "YES";
	return "NO";
}

int main(){
   int i;
	vector<int> lst1(4);
	for (i=0; i < 4 ; ++i){
		lst1.at(i) = rand() % 12 + 1;
	}
	printf("Lst1: ");
   for (i=0; i < 4 ; ++i) printf("%d, ", lst1[i]);
   printf("\n");
	vector<int> lst2(4);
	for (i = 0 ; i < 4 ; ++i){
		lst2.at(i) = rand() % 12 + 1;
	}
	printf("Lst2: ");
   for (i=0; i< 4 ;++i) printf("%d, ", lst2[i]);
   printf("\n");
	int n=exchange(lst1, lst2);