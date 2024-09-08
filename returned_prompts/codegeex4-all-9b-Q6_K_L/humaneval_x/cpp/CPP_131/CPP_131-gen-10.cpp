#include <string>
using namespace std;

int digits(int n){
    string s = to_string(n);
    int product = 1;
    for (char c : s) {
        int digit = c - '0';
        if (digit % 2 != 0) {
            product *= digit;
        }
    }
    return product;
}

B:
#include <string>
using namespace std;

int digits(int n){
    string s = to_string(n);
    int product = 1;
    for (char c : s) {
        int digit = c - '0';
        if (digit % 2 != 0) {
            product *= digit;
        }
    }
    if (product == 1) {
        return 0;
    }
    return product;
}

C:
#include <string>
using namespace std;

int digits(int n){
    string s = to_string(n);
    int product = 1;
    for (char c : s) {
        int digit = c - '0';
        if (digit % 2 != 0) {
            product *= digit;
        }
    }
    if (product == 0) {
        return 0;
    }
    return product;
}

D:
#include <string>
using namespace std;

int digits(int n){
    string s = to_string(n);
    int product = 1;
    for (char c : s) {
        int digit = c - '0';
        if (digit % 2 == 0) {
            product = 0;
        }
    }
    return product;
}

E:
#include <string>
using namespace std;

int digits(int n){
    string s = to_string(n);
    int product = 1;
    for (char c : s) {
        int digit = c - '0';
        if (digit % 2 == 0) {
            product = 0;
        }
    }
    if (product == 0) {
        return 1;
    }
    return product;
}

F:
#include <string>
using namespace std;

int digits(int n){
    string s = to_string(n);
    int product = 1;
    for (char c : s) {
        int digit = c - '0';
        if (digit % 2 == 1) {
            product *= digit;
        }
    }
    return product;
}

G:
#include <string>
using namespace std;

int digits(int n){
    string s = to