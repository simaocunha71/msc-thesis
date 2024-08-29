#include<stdio.h>
#include<math.h>
#include<vector>
using namespace std;
vector<float> derivative(vector<float> xs){
    int len = xs.size();
    vector<float> result;
    for(int i = 0; i<len-1; i++){
        result.push_back(xs[i]*i);
    }
    return result;
}

B:
#include<stdio.h>
#include<math.h>
#include<vector>
using namespace std;
vector<float> derivative(vector<float> xs){
    int len = xs.size();
    vector<float> result;
    for(int i = 0; i<len-1; i++){
        result.push_back(xs[i]*i);
    }
    return result;
}

C:
#include<stdio.h>
#include<math.h>
#include<vector