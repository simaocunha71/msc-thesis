
You have a lot of code in the global namespace, which is generally considered bad practice.  Consider putting all your code inside a namespace.  That would look something like this:
#include<stdio.h>
#include<math.h>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;

namespace MyNamespace {
    bool has_close_elements(vector<float> numbers, float threshold){
        // code here
    }

    vector<string> separate_paren_groups(string paren_string){
        // code here
    }

    float truncate_number(float number){
        // code here
    }

    int count_distinct_characters(string str){ 
        // code here
    }
}

I would also recommend putting all your code inside functions.  You could, for example, create a main function that calls your other functions and prints the results.  That would look something like this:
int main() {
    printf("%d\n", MyNamespace::has_close_elements({1.0, 2.0, 3.0}, 0.5));
    printf("%d\n", MyNamespace::has_close_elements({1.0, 2.8, 3.0, 4.0, 5.0, 2.0}, 0.3));
    printf("%s\n", MyNamespace::separate_paren_groups("( ) (( )) (( )( ))").c_str());
    printf("%s\n", MyNamespace::separate_paren_groups("(())(()())").c_str());
    printf("%f\n", MyNamespace::truncate_number(3.5));
    printf("%d\n", MyNamespace::count_distinct_characters("Jerry"));
    return 0;
}

I would also recommend using the standard C++ library functions instead of the C functions.  For example, instead of using printf, you could use cout and endl.  That would look something like this:
#include<cstdio>
#include<cmath>
#include<vector>
#include<string>
#include<algorithm>
#include<iostream>

namespace MyNamespace {
    bool has_close_elements(vector<float> numbers, float threshold){
