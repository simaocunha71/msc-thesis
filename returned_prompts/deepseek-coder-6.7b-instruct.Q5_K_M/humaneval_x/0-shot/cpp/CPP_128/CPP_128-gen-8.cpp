    int productSign = 1;
    int sum = 0;

    if (arr.empty())
        return -32768;

    for (int i=0; i<arr.size(); i++) {
        if (arr[i] < 0)
            productSign *= -1;
        sum += abs(arr[i]);
    }
    return productSign * sum;
}

*/

//cpp
#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

int prod_signs(vector<int> arr){
    int productSign = 1;
    int sum = 0;

    if (arr.empty())
        return -32768;

    for (int i=0; i<arr.size(); i++) {
        if (arr[i] < 0)
            productSign *= -1;
        sum += abs(arr[i]);
    }
    return productSign * sum;
}

int main() {
    vector<int> arr = {1, 2, 2, -4};
    cout << prod_signs(arr) << endl; //outputs: -9
    return 0;
}

//C++ Solution
/*
