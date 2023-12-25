/*
Given a positive integer n, return a vector that has the number of even and odd
integer palindromes that fall within the range(1, n), inclusive.

Example 1:

    Input: 3
    Output: (1, 2)
    Explanation:
    Integer palindrome are 1, 2, 3. one of them is even, and two of them are odd.

Example 2:

    Input: 12
    Output: (4, 6)
    Explanation:
    Integer palindrome are 1, 2, 3, 4, 5, 6, 7, 8, 9, 11. four of them are even, and 6 of them are odd.

Note:
    1. 1 <= n <= 10^3
    2. returned vector has the number of even and odd integer palindromes respectively.
*/
#include<stdio.h>
#include<vector>
#include<string>
using namespace std;
vector<int> even_odd_palindrome(int n){
	vector<int> ans;
	for(int i = 0;i < n ;i++){
		if(( (i +1) % 2 ) == 0 ){
			ans.push_back(i);
		}else{
			continue;
		}
	}
	for(int i = 0; i < n ;i++){
		if(( (i +1) % 2 ) == 1 ){
			ans.push_back(i);
		}else{
			continue;
		}
	}
	return ans;
}
int main(){
    int n = 30, j=0;
    vector<int> a = even_odd_palindrome(n);
    for (unsigned int i=0;i<a.size();++i){
        printf("%d ",a[i]);
    }
	printf("\n");
}
