#include<stdio.h>
#include<string>
using namespace std;
int fruit_distribution(string s,int n){

    int apples=0,oranges=0,mango=0,sum=0;
    for(int i=0;i<s.length();i++){
        if(s[i]=='a'){apples++;}
        else if(s[i]=='o'){oranges++;}
    }
    mango=n-apples-oranges;
    return mango;
}
int main(){
    string s;
    int n;
    scanf("%s%d",&s,&n);
    printf("%d\n",fruit_distribution(s,n));
    return 0;
}






































































































































































