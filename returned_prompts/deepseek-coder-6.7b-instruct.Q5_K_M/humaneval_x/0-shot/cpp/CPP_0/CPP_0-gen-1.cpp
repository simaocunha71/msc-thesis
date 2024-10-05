    for (int i = 0; i < numbers.size(); i++){
        for (int j = i + 1; j < numbers.size(); j++){
            if(fabs(numbers[j] - numbers[i]) < threshold){
                return true;
            }
        }
    }
    return false;
}

int main(){
    vector<float> numbers1 = {1.0, 2.0, 3.0};
    vector<float> numbers2 = {1.0, 2.8, 3.0, 4.0, 5.0, 2.0};

    printf(has_close_elements(numbers1, 0.5) ? "true" : "false");
    printf(has_close_elements(numbers2, 0.3) ? "true" : "false");

    return 0;
}

*/

#include<stdio.h>
#include<vector>
#include<math.h>
using namespace std;
bool has_close_elements(vector<float> numbers, float threshold){
    for (int i = 0; i < numbers.size(); i++){
        for (int j = i + 1; j < numbers.size(); j++){
            if(fabs(numbers[j] - numbers[i]) < threshold){
                return true;
            }
        }
    }
    return false;
}

int main(){
    vector<float> numbers1 = {1.0, 2.0, 3.0};
    vector<float> numbers2 = {1.0, 2.8, 3.0, 4.0, 5.0, 2.0};

    printf(has_close_elements(numbers1, 0.5) ? "true" : "false");
    printf(has_close_elements(numbers2, 0.3) ? "true" : "false");

    return 0;
}

*/

#include<stdio.h>
#include<vector>
#include<math.h>
using namespace std;
bool has_close_elements(vector<