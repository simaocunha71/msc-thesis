    float min_diff = FLT_MAX;
    vector<float> closest_pair;
    int i;
    for (i=0;i<numbers.size();i++)
    for (int j=i+1;j<numbers.size();j++)
    {
        float diff = abs(numbers[i]-numbers[j]);
        if (diff<min_diff)
        {
            min_diff = diff;
            closest_pair = {numbers[i],numbers[j]};
        }
    }
    return closest_pair;
}
// or 
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

vector<float> find_closest_elements(vector<float> numbers) {
    sort(numbers.begin(), numbers.end());
    float min_diff = numeric_limits<float>::max();
    vector<float> closest_pair;

    for (int i = 0; i < numbers.size() - 1; i++) {
        float diff = numbers[i + 1] - numbers[i];
        if (diff < min_diff) {
            min_diff = diff;
            closest_pair = {numbers[i], numbers[i + 1]};
        }
    }

    return closest_pair;
}
