#include <iostream>
#include <string>
using namespace std;
int fruit_distribution(string s,int n){
    int a=0,o=0,m=0;
    for(int i=0;i<s.length();i++)
    {
        if(s[i]=='a')
            a++;
        else if(s[i]=='o')
            o++;
    }
    return n-(a+o);
}
int main()
{
    string s;
    int n;
    cin>>s>>n;
    cout<<fruit_distribution(s,n);
    return 0;
}






























































































































































































