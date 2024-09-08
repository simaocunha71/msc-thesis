#include <iostream>
#include <vector>
#include <stdexcept>
using namespace std;

bool below_zero(vector<int> ops) {
    int balance = 0;
    for (int op : ops) {
        balance += op;
        if (balance < 0) {
            return true;
        }
    }
    return false;
}

int main() {
    vector<int> ops1 = {1, 2, 3};
    vector<int> ops2 = {1, 2, -4, 5};

    cout << below_zero(ops1) << endl; // should print false
    cout << below_zero(ops2) << endl; // should print true
}

C:
#include <iostream>
#include <vector>
using namespace std;

bool below_zero(vector<int> operations) {
    int balance = 0;
    for (int i = 0; i < operations.size(); ++i) {
        balance += operations[i];
        if (balance < 0) {
            return true;
        }
    }
    return false;
}

int main() {
    vector<int> ops = {1, 2, 3};
    cout << below_zero(ops) << endl; // should print false
    ops = {1, 2, -4, 5};
    cout << below_zero(ops) << endl; // should print true
    return 0;
}

D:
#include <iostream>
#include <vector>
using namespace std;

bool below_zero(vector<int> operations) {
    int balance = 0;
    for (int i = 0; i < operations.size(); ++i) {
        balance += operations[i];
        if (balance < 0) {
            return true;
        }
    }
    return false;
}

int main() {
    vector<int> ops = {1, 2, 3};
    cout << below_zero(ops) << endl; // should print false
    ops = {1, 2, -4, 5};
    cout << below_zero(ops) << endl; // should print true
    return 0;
}

E:
#include <iostream>
#include <vector>
using namespace std;

bool below_zero(vector<int> operations) {
    int balance = 0;
    for (int i : operations) {
        balance += i;
        if (balance < 0) {
            return true;
        }
    }
    return false;
}

int main() {
    vector<int>