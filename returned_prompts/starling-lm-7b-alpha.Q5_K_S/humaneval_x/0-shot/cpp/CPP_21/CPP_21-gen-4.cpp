    float min_number = *min_element(numbers.begin(), numbers.end());
    float max_number = *max_element(numbers.begin(), numbers.end());
    for(int i = 0; i < numbers.size(); i++) {
        numbers[i] = (numbers[i] - min_number) / (max_number - min_number);
    }
    return numbers;
}

#include <bits/stdc++.h>
using namespace std;

vector<float> rescale_to_unit(vector<float> numbers) {
    float min_number = *min_element(numbers.begin(), numbers.end());
    float max_number = *max_element(numbers.begin(), numbers.end());
    for (int i = 0; i < numbers.size(); i++) {
        numbers[i] = (numbers[i] - min_number) / (max_number - min_number);
    }
    return numbers;
}

int main() {
    vector<float> numbers = {1.0, 2.0, 3.0, 4.0, 5.0};
    vector<float> result = rescale_to_unit(numbers);
    for (float num : result) {
        printf("%.2f ", num);
    }
    return 0;
}

*/

#include <bits/stdc++.h>
using namespace std;

vector<float> rescale_to_unit(vector<float> numbers) {
    float min_number = *min_element(numbers.begin(), numbers.end());
    float max_number = *max_element(numbers.begin(), numbers.end());
    for (int i = 0; i < numbers.size(); i++) {
        numbers[i] = (numbers[i] - min_number) / (max_number - min_number);
    }
    return numbers;
}

int main() {
    vector<float> numbers = {1.0, 2.0, 3.0, 4.0, 5.0};
    vector<float> result = rescale