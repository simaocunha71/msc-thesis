#include<stdio.h>
#include<math.h>
#include<vector>
using namespace std;
vector<float> derivative(vector<float> xs){
    vector<float> result;
    float n = xs.size();
    for(int i=1;i<n;i++){
        result.push_back(xs[i]*i);
    }
    return result;
}
