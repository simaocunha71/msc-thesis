    vector<float> result;
    int i;
    for (i=1;i<xs.size();i++)
    {
        result.push_back(xs[i]*i);
    }
    return result;
}
// Alternative Solution
#include<stdio.h>
#include<math.h>
#include<vector>
using namespace std;
vector<float> derivative(vector<float> xs){
    vector<float> result;
    result.push_back(0);
    for (int i=1;i<xs.size()-1;i++)
    {
        result.push_back(xs[i]*i);
    }
    return result;
}
// Alternative Solution
#include<stdio.h>
#include<math.h>
#include<vector>
using namespace std;
vector<float> derivative(vector<float> xs){
    return vector<float>(xs.begin()+1,xs.end());
}
// Alternative Solution
#include<stdio.h>
#include<math.h>
#include<vector>
using namespace std;
vector<float> derivative(vector<float> xs){
    return vector<float>(1,xs.end()-1);
}