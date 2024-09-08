    if(interval1[1]<interval2[0] || interval2[1]<interval1[0]){
        return "NO";
    }
    int start = max(interval1[0],interval2[0]);
    int end = min(interval1[1],interval2[1]);
    if(end-start==1){
        return "NO";
    }
    for(int i = 2; i * i <= end - start; i++) {
        if((end - start) % i == 0) {
            return "NO";
        }
    }
    return "YES";
}
int main() {
    vector<int> interval1 = {1, 3};
    vector<int> interval2 = {2, 4};
    printf("%s\n", intersection(interval1, interval2).c_str()); 
    return 0;
}
*/


Solution:
The problem is to find whether the length of intersection of two intervals is a prime number or not. 

Here is a simple solution in C++. 

We first check if the intervals intersect or not. If they don't intersect, we return "NO". 

If they do intersect, we find the start and end of the intersection. 

Then we check if the length of the intersection is a prime number by trying to divide it by all numbers less than its square root. 

If it is not divisible by any of these numbers, it is a prime number and we return "YES". 

If it is divisible by any of these numbers, it is not a prime number and we return "NO".

Here is the code:

```c++
#include<stdio.h>
#include<vector>
#include<string>
using namespace std;
string intersection( vector<int> interval1,vector<int> interval2){
    if(interval1[1]<interval2[0] || interval2[1]<interval1[0]){
        return "NO";
    }
    int start = max(interval1[0],interval2[0]);
    int end = min(interval1[1],interval2[1]);
    if(end-start==1){
        return "NO";
    }
    for(int i = 2; i * i <= end - start; i++) {
        if((end - start) % i == 0) {
            return "NO";
        }
    }
    return "YES";
}
int main() {
    vector<int> interval1 = {1, 3};
    vector<int> interval2 = {2, 4};
    printf("%s\n