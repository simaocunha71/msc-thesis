    vector<int> max_vector;

    int max = numbers[0];
    max_vector.push_back(max);

    for(int i = 1; i < numbers.size(); i++) {
        if(numbers[i] > max) {
            max = numbers[i];
        }
        max_vector.push_back(max);
    }

    return max_vector;
}

int main() {
    vector<int> numbers = {1, 2, 3, 2, 3, 4, 2};
    vector<int> result = rolling_max(numbers);
    for(int i = 0; i < result.size(); i++) {
        printf("%d ", result[i]);
    }
    printf("\n");
    return 0;
}

B:
#include <iostream>
#include <vector>
using namespace std;

vector<int> rolling_max(vector<int> numbers) {
    vector<int> max_vector;
    int max = numbers[0];
    max_vector.push_back(max);
    for(int i = 1; i < numbers.size(); i++) {
        max = max > numbers[i] ? max : numbers[i];
        max_vector.push_back(max);
    }
    return max_vector;
}

int main() {
    vector<int> numbers = {1, 2, 3, 2, 3, 4, 2};
    vector<int> result = rolling_max(numbers);
    for(int i = 0; i < result.size(); i++) {
        cout << result[i] << " ";
    }
    cout << "\n";
    return 0;
}C:
#include <iostream>
#include <vector>
using namespace std;

vector<int> rolling_max(vector<int> numbers) {
    vector<int> max_vector;
    int max = numbers[0];
    max_vector.push_back(max);
    for(int i = 1; i < numbers.size(); i++) {
        max = max > numbers[i] ? max : numbers[i];
        max_vector.push_back(max);
    }
    return max_vector;
}

int main() {
    vector<int> numbers = {1, 2, 3, 2, 3, 4, 2};
    vector<int> result = rolling_max(numbers);
    for(int i = 0; i < result.size(); i++) {
        cout << result[i] << " ";
    }
    cout << "\n";
    return 0;
}
D:
#include <iostream>
#include <vector>
using namespace std;

vector<int> rolling_max(vector