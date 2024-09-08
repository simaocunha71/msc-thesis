#include<stdio.h>
#include<math.h>
#include<vector>
using namespace std;
int max_element(vector<int> l){
    int max = 0;
    for(int i = 0; i < l.size(); i++){
        if(l[i] > max){
            max = l[i];
        }
    }
    return max;
}

