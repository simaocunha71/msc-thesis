#include <iostream>
#include <vector>
#include <cmath>
#include <string>
using namespace std;

bool has_close_elements(vector<float> numbers, float threshold) {
    for (int i = 0; i < numbers.size(); i++) {
        for (int j = i + 1; j <