    string s = to_string(x);
    if(shift >= s.size()){
        reverse(s.begin(),s.end());
        return s;
    }
    else{
        rotate(s.rbegin(),s.rbegin()+shift,s.rend());
        return s;
    }
}
int main(){
    printf("%s\n",circular_shift(12,1).c_str());
    printf("%s\n",circular_shift(12,2).c_str());
    return 0;
}

*/

//src/main.cpp
#include <iostream>
#include "circular_shift.cpp"
using namespace std;

int main() {
    cout << circular_shift(12, 1) << endl;
    cout << circular_shift(12, 2) << endl;
    return 0;
}

//tests/test_circular_shift.cpp
#define CATCH_CONFIG_MAIN  // This tells Catch to provide a main() - only do this in one cpp file
#include "catch.hpp"
#include "../src/circular_shift.cpp"

TEST_CASE("Testing circular_shift function") {
    REQUIRE(circular_shift(12, 1) == "21");
    REQUIRE(circular_shift(12, 2) == "12");
}

//tests/test_main.cpp
#define CATCH_CONFIG_MAIN  // This tells Catch to provide a main() - only do this in one cpp file
#include "catch.hpp"
#include "../src/main.cpp"

TEST_CASE("Testing main function") {
    // This test is not applicable for this problem
    // REQUIRE(main() == 0);
}