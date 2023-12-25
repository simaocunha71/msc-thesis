/*
Everyone knows Fibonacci sequence, it was studied deeply by mathematicians in 
the last couple centuries. However, what people don't know is Tribonacci sequence.
Tribonacci sequence is defined by the recurrence:
tri(1) = 3
tri(n) = 1 + n / 2, if n is even.
tri(n) =  tri(n - 1) + tri(n - 2) + tri(n + 1), if n is odd.
For example:
tri(2) = 1 + (2 / 2) = 2
tri(4) = 3
tri(3) = tri(2) + tri(1) + tri(4)
       = 2 + 3 + 3 = 8 
You are given a non-negative integer number n, you have to a return a vector of the 
first n + 1 numbers of the Tribonacci sequence.
Examples:
tri(3) = {1, 3, 2, 8}
*/
#include<stdio.h>
#include<vector>
using namespace std;
vector<int> tri(int n){
	if(n < 0) return vector<int>();
    int vector[10];
    vector[0] = vector[1]= vector[2]= 3;//init vector with 3,2,1
    if (n%2==1)
      {vector[4+i]= vector[1+i]+vector[2+i]+vector[4-2+2*i];} //calculate the vector[k] where k is odd.
    else vector[4+i]= vector[1+i]+vector[2+i]+vector[3+2*i];//calculate the vector[k] where k is even.
    return vector;
}
int main(){
	int n = 0 ;
   int i=0;
   while(n<1)
        {cout<<"Enter n :";cin>>n;}
   cout << tri(n).size() << endl;
   if(tri(i))
     {for (unsigned k=3+4*i;k!=2;k++)
             {if((k