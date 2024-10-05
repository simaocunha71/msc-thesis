    int balance = 0;
    for(auto i: operations){
        balance += i;
        if(balance<0){
            return true;
        }
    }
    return false;
}

int main(){
    vector<int> a = {1, 2, 3};
    vector<int> b = {1, 2, -4, 5};
    printf(below_zero(a)? "true\n" : "false\n");
    printf(below_zero(b)? "true\n" : "false\n");
    return 0;
}
*/

//C++/main.cpp
#include <iostream>
#include<vector>
#include "BankAccount.h"
using namespace std;

int main()
{
    vector<int> ops = {100, 200, -50, 300, -100, 50};
    BankAccount account;
    for(auto op: ops){
        account.processOperation(op);
        if(account.isNegative()){
            cout<< "Balance fell below zero at: " << op << endl;
            break;
        }
    }
    if(!account.isNegative()){
        cout<< "Balance never fell below zero." << endl;
    }
    return 0;
}

//C++/BankAccount.cpp
#include "BankAccount.h"

BankAccount::BankAccount()
{
    balance = 0;
}

void BankAccount::processOperation(int op)
{
    balance += op;
}

bool BankAccount::isNegative()
{
    return balance < 0;
}

//C++/BankAccount.h
#pragma once
#include "main.cpp"

class BankAccount
{
private:
    int balance;
public:
    BankAccount();
    void processOperation(int op);
    bool isNegative();
};

//C++/main.h
#pragma once
#include "BankAccount.h"

int main();

//C++/main.h
