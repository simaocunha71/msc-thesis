    int left = 0;
    int right = 0;
    for(int i = 0; i < brackets.size(); i++) {
        if(brackets[i] == '<') {
            left++;
        } else {
            right++;
        }
    }
    if (left != right) {
        return false;
    }
    return true;
}

int main() {
    printf("%d\n", correct_bracketing("<")); // false
    printf("%d\n", correct_bracketing("<>")); // true
    printf("%d\n", correct_bracketing("<<><>>")); // true
    printf("%d\n", correct_bracketing("><<>")); // false
    return 0;
}
B:
#include<stdio.h>
#include<string>
using namespace std;
bool correct_bracketing(string brackets){
    int left = 0;
    int right = 0;
    for(int i = 0; i < brackets.size(); i++) {
        if(brackets[i] == '<') {
            left++;
        } else {
            right++;
        }
    }
    if (left != right) {
        return false;
    }
    return true;
}

int main() {
    printf("%d\n", correct_bracketing("<")); // false
    printf("%d\n", correct_bracketing("<>")); // true
    printf("%d\n", correct_bracketing("<<><>>")); // true
    printf("%d\n", correct_bracketing("><<>")); // false
    return 0;
}
C:
#include<stdio.h>
#include<string>
using namespace std;
bool correct_bracketing(string brackets){
    int left = 0;
    int right = 0;
    for(int i = 0; i < brackets.size(); i++) {
        if(brackets[i] == '<') {
            left++;
        } else {
            right++;
        }
    }
    if (left != right) {
        return false;
    }
    return true;
}

int main() {
    printf("%d\n", correct_bracketing("<")); // false
    printf("%d\n", correct_bracketing("<>")); // true
    printf("%d\n", correct_bracketing("<<><>>")); // true
    printf("%d\n", correct_bracketing("><<>")); // false
    return 0;
}
D:
#include<stdio.h>
#include<string>
using namespace std;
bool correct_bracketing(string brackets){
    int