#include <iostream>
#include <cmath>
#include <vector>

using namespace std;

bool has_close_elements(vector<float> numbers, float threshold){
    for(int i = 0; i < numbers.size(); i++){
        for(int j = i + 1; j < numbers.size(); j++){
            if(abs(numbers[i] - numbers[j]) < threshold){
                return true;
            }
        }
    }
    return false;
}

int main(){
    vector<float> numbers1 = {1.0, 2.0, 3.0};
    vector<float> numbers2 = {1.0, 2.8, 3.0, 4.0, 5.0, 2.0};

    cout << has_close_elements(numbers1, 0.5) << endl; // false
    cout << has_close_elements(numbers2, 0.3) << endl; // true

    return 0;
}

B:
#include <iostream>
#include <cmath>
#include <vector>

using namespace std;

bool has_close_elements(vector<float> numbers, float threshold){
    for(int i = 0; i < numbers.size(); i++){
        for(int j = i + 1; j < numbers.size(); j++){
            if(abs(numbers[i] - numbers[j]) < threshold){
                return true;
            }
        }
    }
    return false;
}

int main(){
    vector<float> numbers1 = {1.0, 2.0, 3.0};
    vector<float> numbers2 = {1.0, 2.8, 3.0, 4.0, 5.0, 2.0};

    cout << has_close_elements(numbers1, 0.5) << endl; // false
    cout << has_close_elements(numbers2, 0.3) << endl; // true

    return 0;
}

C:
#include <iostream>
#include <cmath>
#include <vector>

using namespace std;

bool has_close_elements(vector<float> numbers, float threshold){
    for(int i = 0; i < numbers.size(); i++){
        for(int j = i + 1; j < numbers.size(); j++){
            if(abs(numbers[i] - numbers[j]) < threshold){
                return true;
            }
        }
    }
    return false;
}

int main(){
    vector<float> numbers1 = {1.0, 2.0, 3.0};
    vector<float