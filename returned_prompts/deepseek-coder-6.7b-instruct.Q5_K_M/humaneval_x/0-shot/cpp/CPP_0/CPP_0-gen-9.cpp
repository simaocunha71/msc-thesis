    for(int i=0; i < numbers.size()-1; i++){
        for(int j=i+1; j < numbers.size(); j++){
            if(fabs(numbers[i] - numbers[j]) < threshold){
                return true;
            }
        }
    }
    return false;
}

int main() {
    vector<float> numbers1 = {1.0, 2.0, 3.0};
    vector<float> numbers2 = {1.0, 2.8, 3.0, 4.0, 5.0, 2.0};
    printf("%d\n", has_close_elements(numbers1, 0.5)); // false
    printf("%d\n", has_close_elements(numbers2, 0.3)); // true
    return 0;
}
*/

int main(void) {
    printf("%d\n", has_close_elements((vector<float>){1.0, 2.0, 3.0}, 0.5)); // false
    printf("%d\n", has_close_elements((vector<float>){1.0, 2.8, 3.0, 4.0, 5.0, 2.0}, 0.3)); // true
    return 0;
}
*/

#include<stdio.h>
#include<vector>
#include<math.h>
using namespace std;
bool has_close_elements(vector<float> numbers, float threshold){
    for(int i=0; i < numbers.size()-1; i++){
        for(int j=i+1; j < numbers.size(); j++){
            if(fabs(numbers[i] - numbers[j]) < threshold){
                return true;
            }
        }
    }
    return false;
}

int main() {
    printf("%d\n", has_close_elements({1.0, 2.0, 3.0}, 0.5)); // false
    printf("%d\n", has_close_elements({1.0, 2.8