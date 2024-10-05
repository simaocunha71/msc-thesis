    long long factorial = 1;

    for(int i = 1; i <= n; i++){
        factorial *= i;
    }

    return factorial;
}

int main(){
    int n;
    scanf("%d",&n);
    printf("%lld\n",special_factorial(n));
    return 0;
}

*/

//C++/factorial.cpp
#include<stdio.h>
using namespace std;
long long special_factorial(int n){

    long long factorial = 1;

    for(int i = 1; i <= n; i++){
        factorial *= i;
    }

    return factorial;
}

int main(){
    int n;
    scanf("%d",&n);
    printf("%lld\n",special_factorial(n));
    return 0;
}

//C++/factorial_test.cpp
#define CATCH_CONFIG_MAIN  // This tells Catch to provide a main() - only do this in one cpp file
#include "catch.hpp"
#include "factorial.cpp"

TEST_CASE("Factorials are computed", "[factorial]"){
    REQUIRE(special_factorial(0) == 1);
    REQUIRE(special_factorial(1) == 1);
    REQUIRE(special_factorial(2) == 2);
    REQUIRE(special_factorial(3) == 6);
    REQUIRE(special_factorial(10) == 3628800);
}

//C++/factorial_test.hpp
#define CATCH_CONFIG_MAIN  // This tells Catch to provide a main() - only do this in one cpp file
#include "catch.hpp"
#include "factorial.cpp"

TEST_CASE("Factorials are computed", "[factorial]"){
    REQUIRE(special_factorial(0) == 1);
    REQUIRE(special_factorial(1) == 1);
    REQUIRE(special_factorial(2) == 2);
