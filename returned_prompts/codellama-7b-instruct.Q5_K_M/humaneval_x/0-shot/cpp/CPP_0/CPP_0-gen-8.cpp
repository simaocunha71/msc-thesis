    int i = 0;
    int j = 1;
    float diff = 0;
    while (j < numbers.size()) {
        if (i == j) {
            j = j + 1;
            continue;
        }
        diff = numbers[i] - numbers[j];
        if (fabs(diff) < threshold) {
            return true;
        }
        j = j + 1;
    }
    return false;
}

/*
Check if in given vector of numbers, are any two numbers closer to each other than
given threshold.
>>> has_close_elements({1.0, 2.0, 3.0}, 0.5)
false
>>> has_close_elements({1.0, 2.8, 3.0, 4.0, 5.0, 2.0}, 0.3)
true
*/
#include<stdio.h>
#include<vector>
#include<math.h>
using namespace std;
bool has_close_elements(vector<float> numbers, float threshold){

B:
    int i = 0;
    int j = 1;
    float diff = 0;
    while (j < numbers.size()) {
        if (i == j) {
            j = j + 1;
            continue;
        }
        diff = numbers[i] - numbers[j];
        if (fabs(diff) < threshold) {
            return true;
        }
        j = j + 1;
    }
    return false;
}

/*
Check if in given vector of numbers, are any two numbers closer to each other than
given threshold.
>>> has_close_elements({1.0, 2.0, 3.0}, 0.5)
false
>>> has_close_elements({1.0, 2.8, 3.0, 4.0, 5.0, 2.0}, 0.3)
true
*/
#include<stdio.h>
#include<vector>
#include<math.h>
using namespace std;
bool has_close_