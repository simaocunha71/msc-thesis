#include<stdio.h>
#include<vector>
using namespace std;
vector<int> generate_integers(int a,int b){
vector<int> result;
int start = a;
int end = b;
if (start > end) {
    start = b;
    end = a;
}
for (int i = start; i <= end; i++) {
    int num = i;
    while (num > 0) {
        int digit = num % 10;
        if (digit % 2 == 0) {
            result.push_back(digit);
        }
        num /= 10;
    }
}
return result;
}

