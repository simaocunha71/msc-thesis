    /*
    Write your code here
    */
}

int main()
{
    vector<string> operato = {"+", "*", "-"};
    vector<int> operand = {2, 3, 4, 5};
    printf("%d\n", do_algebra(operato, operand));
    return 0;
}

*/

#include <vector>
#include <string>

int do_algebra(std::vector<std::string> operato, std::vector<int> operand){
    int result = operand[0];
    for(int i=1; i<operand.size(); i++){
        if(operato[i-1]=="+")
            result += operand[i];
        else if(operato[i-1]=="-")
            result -= operand[i];
        else if(operato[i-1]=="*")
            result *= operand[i];
        else if(operato[i-1]=="/")
            result /= operand[i];
        else if(operato[i-1]=="**")
            result = pow(result, operand[i]);
    }
    return result;
}

//src/main.cpp
#include <iostream>
#include <vector>
#include <string>
#include "do_algebra.cpp"

int main()
{
    std::vector<std::string> operato = {"+", "*", "-"};
    std::vector<int> operand = {2, 3, 4, 5};
    std::cout << do_algebra(operato, operand) << std::endl;
    return 0;
}

//test/test.cpp
#include "../src/do_algebra.cpp"
#include <gtest/gtest.h>

TEST(DoAlgebraTest, HandlesBasicAlgebraOperations) {
    std::vector<std::string> operato = {"+", "*", "-"};
    std::vector<int> operand = {2, 3, 4, 5