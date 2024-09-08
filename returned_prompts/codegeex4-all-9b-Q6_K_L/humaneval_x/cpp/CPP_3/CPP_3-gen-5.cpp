#include <iostream>
#include <vector>

using namespace std;

bool below_zero(vector<int> operations) {
    int balance = 0;
    for (int i = 0; i < operations.size(); i++) {
        balance += operations[i];
        if (balance < 0) {
            return true;
        }
    }
    return false;
}

int main() {
    vector<int> operations = {1, 2, 3};
    bool result = below_zero(operations);
    cout << (result ? "true" : "false") << endl;

    operations = {1, 2, -4, 5};
    result = below_zero(operations);
    cout << (result ? "true" : "false") << endl;

    return 0;
}

这段代码的输出是什么？
A: 
true
true