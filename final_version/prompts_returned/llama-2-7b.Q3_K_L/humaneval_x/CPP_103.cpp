/*
You are given two positive integers n and m, and your task is to compute the
average of the integers from n through m (including n and m). 
Round the answer to the nearest integer(smaller one) and convert that to binary.
If n is greater than m, return "-1".
Example:
rounded_avg(1, 5) => "11"
rounded_avg(7, 5) => "-1"
rounded_avg(10, 20) => "1111"
rounded_avg(20, 33) => "11010"
*/
#include<stdio.h>
#include<math.h>
#include<string>
using namespace std;
string rounded_avg(int n,int m){
	if(n>m) return "-1";
	int a =  (pow((double)(n-1),(double)2)+(pow((double)m,(double)2)))/2.0;
	printf("%d\n",a);
	stringstream s;s<<a;
    int avg =0;
	for(int i=0;i<s.str().size();i++) { 
		if(avg%10==9){
			cout<<"1";
		}else{
			if((int)(s.str()[i]-'0')>4 || (int)(s.str()[i]-'0')<2) { 
				avg = avg*10;
        } 
		}
		cout<<(int)(s.str()[i] - '0');	
	}
    return to_string(avg);
}
//Time complexity is O(n+m)
// space complexity is also the same