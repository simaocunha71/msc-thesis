
The first issue I see is that you are not including the standard library namespace in your code. You should add this line to the top of your file:
using namespace std;

The second issue is that your code does not compile because the functions do not have a return type. You need to add a return type to each function. For example, the first function should be:
bool has_close_elements(vector<float> numbers, float threshold) {

The third issue is that you are using the deprecated math.h header. You should replace it with cmath. Also, you should use the standard library functions instead of the deprecated ones. For example, instead of using abs(), you should use std::abs(). The updated code should be:
#include <cmath>
#include <vector>
#include <string>
using namespace std;

bool has_close_elements(vector<float> numbers, float threshold) {
    for (int i = 0; i < numbers.size(); i++) {
        for (int j = i + 1; j < numbers.size(); j++) {
            if (std::abs(numbers[i] - numbers[j]) < threshold) {
                return true;
            }
        }
    }
    return false;
}

The other functions have similar issues. You should fix them in a similar way.