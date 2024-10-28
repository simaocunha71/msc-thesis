    float m=l[0];
    for (int i=1;i<l.size();i++)
    {
        if (l[i]>m)
        m=l[i];
    }
    return m;
}
//OR
#include<algorithm>
float max_element(vector<float> l){
    return *max_element(l.begin(),l.end());
}  // C++11 standard or later
//OR
#include<functional>
float max_element(vector<float> l){
    return *max_element(l.begin(),l.end(),std::less<float>());
}  // C++98 standard or earlier
//OR
#include<iomanip>
#include<limits>
float max_element(vector<float> l){
    float max = numeric_limits<float>::min();
    for (float f : l)
        if (f > max)
            max = f;
    return max;
}  // works with any numeric type that has a min() and max() function
//OR
#include<numeric>
float max_element(vector<float> l){
    return *max_element(l.begin(),l.end(),std::greater<float>());
}  // C++11 standard or later
//OR
#include<iomanip>
#include<limits>
float max_element(vector<float> l){
    float max = numeric_limits<float>::min();
    for (float f : l)
        if (f > max)
            max = f;
    return max;
}  // works with any numeric type that has a min() and max() function
//OR
#include<algorithm>
#include<numeric>
float max_element(vector<float> l){
    return *max_element(l.begin(),l.end(),std::greater<float>());
}  // C++11 standard or later
//OR
#include<numeric>
float max_element(vector<float> l){
    return *max_element(l.begin(),l.end(),std::greater<float>());
}  // C++11 standard or later
//OR
#include<numeric>
float max_element(vector<float> l){
    return *max_element(l.begin(),l.end(),std::greater<float>());
}  // C++11 standard or later
//OR
#include<numeric>
float max_element(vector<float> l){
    return *max_element(l.begin(),l.end(),std::greater<float>());
}  // C++11 standard or later
//OR
#include<numeric>
float max_element(vector<float> l){
    return *max_element(l.begin(),l.end(),std::greater<float>());
}  // C++11 standard or later
//OR