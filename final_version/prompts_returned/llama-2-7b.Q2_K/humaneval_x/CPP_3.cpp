/*
You"re given a vector of deposit and withdrawal operations on a bank account that starts with
zero balance. Your task is to detect if at any point the balance of account falls below zero, and
at that point function should return true. Otherwise it should return false.
>>> below_zero({1, 2, 3})
false
>>> below_zero({1, 2, -4, 5})
true
*/
#include<stdio.h>
#include<vector>
using namespace std;
bool below_zero(vector<int> operations){
	if(operations[0] > operations[operations.size()-1]){ //check max balance of account
		return true;
	}else {
		for (size_t i = 0; i < operations.size(); ++i) { //check for negative balances
			if(operations[i] > operations[i + 1]){ //make sure to check the next operation as well
				return true;
			}else if((!operations[i]) && (operations[i+1])) { //check for negative balances
				return true;
			}
		}
	}
	return false;
}
int main(){
	vector<int> operations = vector<int>(5, 0);
	operations[0] = 1;
	operations[1] = 2;
	operations[2] = -4; //negative deposit
	operations[3] = 5; //positive withdrawal
	if(below_zero(operations)){
		printf("account balance falls below zero at operations[0].\n");
	}else {
		printf("No, account balance stays above zero till operations[operations.size() - 1]\n");
	}
	return 0;
}