#include<stdio.h>
#include<vector>
using namespace std;
vector<int> sum_product(vector<int> numbers){
    int sum = 0;
    int product = 1;
    for(int i = 0; i < numbers.size(); i++){
        sum += numbers[i];
        product *= numbers[i];
    }
    return {sum, product};
}
B:
#include<stdio.h>
#include<vector>
using namespace std;
vector<int> sum_product(vector<int> numbers){
    int sum = 0;
    int product = 1;
    for(int i = 0; i < numbers.size(); i++){
        sum += numbers[i];
        product *= numbers[i];
    }
    return {sum, product};
}

A or B?

The correct answer is A.

The function in answer A is missing a semicolon at the end of the return statement. This is a syntax error in C++ and the code will not compile. The function in answer B is correct and will compile and run without errors.
