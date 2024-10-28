    vector<float> result;
    for (float f : l)
    if (f>0)
    result.push_back(f);
    return result;
}
// or
#include<stdio.h>
#include<math.h>
#include<vector>
using namespace std;
vector<float> get_positive(vector<float> l){
    vector<float> result;
    for (float f : l)
        if (f>0)
            result.push_back(f);
    return result;
} // end of function


