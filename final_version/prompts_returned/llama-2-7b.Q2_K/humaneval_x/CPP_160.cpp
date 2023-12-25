/*
Given two vectors operator, and operand. The first vector has basic algebra operations, and 
the second vector is a vector of integers. Use the two given vectors to build the algebric 
expression and return the evaluation of this expression.

The basic algebra operations:
Addition ( + ) 
Subtraction ( - ) 
Multiplication ( * ) 
Floor division ( // ) 
Exponentiation ( ** ) 

Example:
operator{"+", "*", "-"}
vector = {2, 3, 4, 5}
result = 2 + 3 * 4 - 5
=> result = 9

Note:
    The length of operator vector is equal to the length of operand vector minus one.
    Operand is a vector of of non-negative integers.
    Operator vector has at least one operator, and operand vector has at least two operands.

*/
#include<stdio.h>
#include<math.h>
#include<vector>
#include<string>
using namespace std;
#include<algorithm>
#include<stdlib.h>
int do_algebra(vector<string> operato, vector<int> operand){
	int lop = 0;
	int los=0, los1=0;
	lop = strlen(operator[0].c_str());
    int i=0;
    int j=0;
    string s[5];// for storing the values to the vectors
     //printf("The length of operator vector is equal to the length of operand vector minus one\n");
    
    	if(operato.size() == 1){                          
        printf("operato is a singelton ");
        s[0]=operator[0];
        if(s[0] == ""){return -1;}
        
        else{
            return atoi(s[0].c_str());
        }        
        }else if (operato.size() >= 2){                          
	while((j = find(operator.begin(), operator.end(), operand[i]) != vector<int>::npos) == -1){ //find the result of the algae, or the index
