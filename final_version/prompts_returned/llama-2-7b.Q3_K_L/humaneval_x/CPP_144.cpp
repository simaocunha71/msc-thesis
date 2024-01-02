/*
Your task is to implement a function that will simplify the expression
x * n. The function returns true if x * n evaluates to a whole number and false
otherwise. Both x and n, are string representation of a fraction, and have the following format,
<numerator>/<denominator> where both numerator and denominator are positive whole numbers.

You can assume that x, and n are valid fractions, and do not have zero as denominator.

simplify("1/5", "5/1") = true
simplify("1/6", "2/1") = false
simplify("7/10", "10/2") = false
*/
#include<stdio.h>
#include<string>
using namespace std;
bool simplify(string x,string n){
	int cnt=0;
	if(x==n)//simplify
	{
	return true;
	}else if (isdigit(n[0]))
	{
	cnt++;
	while(isdigit(n[cnt]) || isspace(n[cnt])) { cnt++; }

	if (x.length()==1 && n.length()>x.length()) 
	{
		return false;
	} else if (x.length()>=n.length())
	{
		int j=0;
		while(isdigit(n[j]) || isspace(n[j])) { j++; }

		if (x==n) return true;
		else return false;
	} else if (x>n||x<n)
	{
		return false;
	}
	for(int i=0;i<=cnt-1;i++) //find the remainder of x*n and n/x
	{//cout<<x+'/'<<n<<'\t'<<x+'%'+n%'%<<'\t'<<x+'.0'+n+'.'+1<<endl;
	int m,n1=0,n2=0;
	if((x[i]!='0')&&(i<cnt))//if x is a integer then it is true
	{
		for(m=0;m