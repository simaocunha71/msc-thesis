    //check if the intervals intersect
    if(interval1[1] < interval2[0] || interval2[1] < interval1[0]) return "NO";

B:
    //find the intersection
    int start = max(interval1[0], interval2[0]);
    int end = min(interval1[1], interval2[1]);

C:
    //calculate the length of the intersection
    int len = end - start + 1;

D:
    //check if the length is a prime number
    if(len < 2) return "NO";
    for(int i = 2; i*i <= len; i++){
        if(len % i == 0) return "NO";
    }

E:
    return "YES";
}
int main() {
    vector<int> interval1 = {1, 2};
    vector<int> interval2 = {2, 3};
    cout<<intersection(interval1, interval2)<<endl;
    return 0;
}

*/
#include<iostream>
#include<vector>
#include<string>
using namespace std;

string intersection(vector<int> interval1, vector<int> interval2){
    if(interval1[1] < interval2[0] || interval2[1] < interval1[0]) return "NO";
    
    int start = max(interval1[0], interval2[0]);
    int end = min(interval1[1], interval2[1]);
    
    int len = end - start + 1;
    
    if(len < 2) return "NO";
    for(int i = 2; i*i <= len; i++){
        if(len % i == 0) return "NO";
    }
    return "YES";
}

int main() {
    vector<int> interval1 = {1, 2};
    vector<int> interval2 = {2, 3};
    cout<<intersection(interval1, interval2)<<endl;
    return 0;
}

/*
