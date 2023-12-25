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
	int fx=0,fn=0;
	int rem= 0;
	for (int i=0;i<6;++i) {
        if ((rem = x[5-1-i] - '0') >= 9 ) rem += 9 - 1 ;
     }
    for (int j=0;j<6;++j){
       fn=fn*10 + n[j];
       if (fn%10 == rem) {
		fx = fx * 10;
        fn /= 10;
      } else fn = fn/10;
    }
	if (fx==0 && fn>=0) return true;
	else return false;}
void main(){
int n,x;
string xn;
ifstream fin("input.txt");
cin>>x;
fin >> n;
fin >> xn;
simplify(xn, n);
} 