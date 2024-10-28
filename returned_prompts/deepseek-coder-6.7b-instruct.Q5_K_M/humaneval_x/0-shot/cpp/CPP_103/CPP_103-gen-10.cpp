    if(n>m){
        return "-1";
    }

B:
    int avg=(n+m)/2;
    int rounded_avg=(int)avg;
    if(avg-rounded_avg>=0.5){
        rounded_avg++;
    }

C:
    string binary="";
    while(rounded_avg){
        int bit=rounded_avg%2;
        binary=to_string(bit)+binary;
        rounded_avg/=2;
    }
    return binary;
}

int main(){
    int n,m;
    scanf("%d %d",&n,&m);
    string ans=rounded_avg(n,m);
    printf("%s\n",ans.c_str());
    return 0;
}

*/

#include<stdio.h>
#include<math.h>
#include<string>
using namespace std;
string rounded_avg(int n,int m){
    if(n>m){
        return "-1";
    }
    int avg=(n+m)/2;
    int rounded_avg=(int)avg;
    if(avg-rounded_avg>=0.5){
        rounded_avg++;
    }
    string binary="";
    while(rounded_avg){
        int bit=rounded_avg%2;
        binary=to_string(bit)+binary;
        rounded_avg/=2;
    }
    return binary;
}

int main(){
    int n,m;
    scanf("%d %d",&n,&m);
    string ans=rounded_avg(n,m);
    printf("%s\n",ans.c_str());
    return 0;
}

//C++/rounded_avg.c
/*
