#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

vector<float> rescale_to_unit(vector<float> numbers){
    float min = *min_element(numbers.begin(), numbers.end());
    float max = *max_element(numbers.begin(), numbers.end());
    for(auto &n: numbers){
        n = (n - min) / (max - min);
    }
    return numbers;
}