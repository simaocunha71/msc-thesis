/*
Write your code here.
*/

}

int main(){

vector<int> interval1={1,2};
vector<int> interval2={2,3};
printf("%s\n",intersection(interval1,interval2).c_str());

vector<int> interval3={-1,1};
vector<int> interval4={0,4};
printf("%s\n",intersection(interval3,interval4).c_str());

vector<int> interval5={-3,-1};
vector<int> interval6={-5,5};
printf("%s\n",intersection(interval5,interval6).c_str());

return 0;
}

/*
You are given two intervals,
where each interval is a pair of integers. For example, interval = (start, end) = (1, 2).
The given intervals are closed which means that the interval (start, end)
includes both start and end.
For each given interval, it is assumed that its start is less or equal its end.
Your task is to determine whether the length of intersection of these two 
intervals is a prime number.
Example, the intersection of the intervals (1, 3), (2, 4) is (2, 3)
which its length is 1, which not a prime number.
If the length of the intersection is a prime number, return "YES",
otherwise, return "NO".
If the two intervals don't intersect, return "NO".


{input/output} samples:
intersection({1, 2}, {2, 3}) ==> "NO"
intersection({-1, 1}, {0, 4}) ==> "NO"
intersection({-3, -1}, {-5, 5}) ==> "YES"
*/
#include<stdio.h>
#include<vector>
#include<string>
using namespace std;

bool is_prime(int num){
    if(num<=1)return false;
    if(num==2)return true;
    for(int i=2;i*i<=num;i++){
        if(num%i==0)return false;
    }
    return true;
}

string intersection( vector<int> interval1,vector<int> interval2){

    int start=max(interval1[0],interval2[0]);
    int end=min(interval1[1],interval2[1]);
    if(start>end)return "NO";
    int len=end-start+1;
    if(is_prime(len))return "YES";
    return "NO";

}

int main(){

vector<int> interval1={1,2};
vector<int> interval2={2,