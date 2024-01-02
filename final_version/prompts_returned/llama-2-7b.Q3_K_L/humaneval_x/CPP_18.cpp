/*
Find how many times a given substring can be found in the original string. Count overlaping cases.
>>> how_many_times("", "a")
0
>>> how_many_times("aaa", "a")
3
>>> how_many_times("aaaa", "aa")
3
*/
#include<stdio.h>
#include<string>
using namespace std;
int how_many_times(string str,string substring){
	int n=str.length();
	int m=substring.length(); 
	int count=0;
    for (int i =0;i<=n-m ;++i) {
        if (str[i]==substring[0]){
            int k=1;
            while(i<n && str[i]==substring[k]){
                ++k;
                --i; 
                }
            count+=k-1;
          return count;
        }
    }return 0;
}
int main(){
	string x="aaa";
	cout<<how_many_times(x, "aa")<<endl;
	string y="aaaa";
	cout<<how_many_times(y,"aa")<<endl;
	string z=" ";
    cout<<how_many_times(z, "a")<<endl;
}
