    int unit_a,unit_b;
    unit_a=abs(a%10);
    unit_b=abs(b%10);
    return unit_a*unit_b;

}

int main()
{
    int a,b;
    printf("Enter two numbers: ");
    scanf("%d %d",&a,&b);
    printf("The product of their unit digits is %d",multiply(a,b));
    return 0;
}

//2.cpp
#include<stdio.h>
#include<math.h>
using namespace std;
int multiply(int a,int b){

    int unit_a,unit_b;
    unit_a=abs(a%10);
    unit_b=abs(b%10);
    return unit_a*unit_b;

}

int main()
{
    int a,b;
    printf("Enter two numbers: ");
    scanf("%d %d",&a,&b);
    printf("The product of their unit digits is %d",multiply(a,b));
    return 0;
}

//main.cpp
#include<stdio.h>
#include<math.h>
using namespace std;
int multiply(int a,int b){

    int unit_a,unit_b;
    unit_a=abs(a%10);
    unit_b=abs(b%10);
    return unit_a*unit_b;

}

int main()
{
    int a,b;
    printf("Enter two numbers: ");
    scanf("%d %d",&a,&b);
    printf("The product of their unit digits is %d",multiply(a,b));
    return 0;
}

//test_cases.cpp
#define CATCH_CONFIG_MAIN
#include "catch.hpp"
#include "2.cpp"

TEST_CASE("Testing multiply function"){

    REQUIRE(multiply(148, 412) == 16);
