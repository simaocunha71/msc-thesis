    int sum = 0;
    int len = num.length();
    for(int i=0;i<len;i++){
        if(num[i]=='0'||num[i]=='1'||num[i]=='2'||num[i]=='3'||num[i]=='4'||num[i]=='5'||num[i]=='6'||num[i]=='7'||num[i]=='8'||num[i]=='9'){
            int num1 = num[i]-'0';
            if(num1==2||num1==3||num1==5||num1==7){
                sum++;
            }
        }
        if(num[i]=='A'){
            sum++;
        }
        if(num[i]=='B'){
            sum++;
        }
        if(num[i]=='C'){
            sum++;
        }
        if(num[i]=='D'){
            sum++;
        }
        if(num[i]=='E'){
            sum++;
        }
        if(num[i]=='F'){
            sum++;
        }
    }
    printf("%d\n",sum);
    return sum;
}

int main(void){
    string num;
    while(cin>>num){
        hex_key(num);
    }
    return 0;
}























*/
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cmath>
#include<iostream>
#include<algorithm>
using namespace std;
int main(){
    string str;
    while(cin>>str){
        int sum=0;
        int len=str.length();
        for(int i=0;i<len;i++){
            if(str[i]>='0'&&str[i]<='9'){
                int num1=str[i]-'0';
              