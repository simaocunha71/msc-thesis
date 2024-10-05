    sort(numbers.begin(), numbers.end());
    int len = numbers.size();
    float min_diff = numbers[1] - numbers[0];
    int min_idx = 0;
    for(int i = 1; i < len - 1; ++i){
        float diff = numbers[i+1] - numbers[i];
        if(diff < min_diff){
            min_diff = diff;
            min_idx = i;
        }
    }
    vector<float> result = {numbers[min_idx], numbers[min_idx+1]};
    return result;
}

int main(){
    vector<float> numbers = {1.0, 2.0, 3.0, 4.0, 5.0, 2.2};
    vector<float> res = find_closest_elements(numbers);
    printf("(%f, %f)\n", res[0], res[1]);
    return 0;
}

The code above does the job. It sorts the input vector and iterates over it to find the pair of elements with the smallest difference. This pair of elements are returned in a vector.
*/

#include <iostream>
#include <vector>
#include <algorithm>

std::pair<float, float> find_closest_elements(std::vector<float> numbers) {
    std::sort(numbers.begin(), numbers.end());
    float min_diff = numbers[1] - numbers[0];
    std::pair<float, float> closest_pair = {numbers[0], numbers[1]};
    for (size_t i = 1; i < numbers.size() - 1; ++i) {
        float diff = numbers[i+1] - numbers[i];
        if (diff < min_diff) {
            min_diff = diff;
            closest_pair = {numbers[i], numbers[i+1]};
        }
    }
    return closest_pair;
}

int main() {
    std::vector<float> numbers = {1.0, 2.0, 3.0, 4.0, 5