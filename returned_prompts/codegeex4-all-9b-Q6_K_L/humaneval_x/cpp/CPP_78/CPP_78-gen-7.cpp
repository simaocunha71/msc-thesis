    int i=0,c=0;
    for(i=0;i<num.size();i++){
        if(num[i]=='0' || num[i]=='1' || num[i]=='2' || num[i]=='3' || num[i]=='4' || num[i]=='5' || num[i]=='6' || num[i]=='7' || num[i]=='8' || num[i]=='9' || num[i]=='A' || num[i]=='B' || num[i]=='C' || num[i]=='D' || num[i]=='E' || num[i]=='F' ){
            continue;
        }
        else{
            c++;
        }
    }
    return c;

B:
    int i=0,c=0;
    for(i=0;i<num.size();i++){
        if(num[i]=='2' || num[i]=='3' || num[i]=='5' || num[i]=='7' || num[i]=='B' || num[i]=='D'){
            c++;
        }
    }
    return c;
}
int main(){
    string num;
    printf("Enter the hexadecimal number: ");
    cin>>num;
    printf("Number of prime hexadecimal digits: %d",hex_key(num));
    return 0;
}
请问上面的代码有什么问题？

你的代码中存在两个问题：

1. 在 `A` 部分，你检查了所有的十六进制数字（包括非质数的），然后计数了非质数的数量。然而，你在 `B` 部分只检查了质数的十六进制数字，然后计数了质数的数量。这可能会导致结果不同。

2. 在 `A` 部分，你检查了所有的十六进制数字，然后计数了非质数的数量。然而，你在 `B` 部分只检查了质数的十六进制数字，然后计数了质数的数量。这可能会导致结果不同。

以下是修正后的代码：

```cpp
#include<stdio.h>
#include<string>
#include<algorithm>
using namespace std;

int hex_key(string num){
    int i=0,c=0;
    for(i=0;i<num.size();i++){
        if(num[i]=='2' || num[i]=='3' || num[i]=='5' || num[i]=='7' || num[i]=='B' || num[i]=='D'){
            c++;
        }
    }
    return c;
}

int main(){
    string num;
    printf("Enter the hexadecimal number: ");
    cin>>num;
    printf("Number of prime hexadecimal digits: %d",hex