    int count = 0;
    for(int i = 0; i < brackets.length(); i++){
        if(brackets[i] == '('){
            count++;
        }
        else if(brackets[i] == ')'){
            if(count == 0){
                return false;
            }
            count--;
        }
    }
    if(count != 0){
        return false;
    }
    return true;
}

int main() {
    cout << correct_bracketing("(") << endl;  // false
    cout << correct_bracketing("()") << endl;  // true
    cout << correct_bracketing("(()())") << endl;  // true
    cout << correct_bracketing(")(()") << endl;  // false
    return 0;
}  // false

B:
    #include <iostream>
    #include <string>
    using namespace std;

    bool correct_bracketing(string brackets) {
        int count = 0;
        for (int i = 0; i < brackets.length(); i++) {
            if (brackets[i] == '(') {
                count++;
            }
            else if (brackets[i] == ')') {
                if (count == 0) {
                    return false;
                }
                count--;
            }
        }
        if (count != 0) {
            return false;
        }
        return true;
    }

    int main() {
        cout << correct_bracketing("(") << endl;  // false
        cout << correct_bracketing("()") << endl;  // true
        cout << correct_bracketing("(()())") << endl;  // true
        cout << correct_bracketing(")(()") << endl;  // false
        return 0;
    }

C:
    bool correct_bracketing(string brackets) {
        stack<char> s;
        for (char c : brackets) {
            if (c == '(') {
                s.push(c);
            } else if (c == ')') {
                if (s.empty()) {
                    return false;
                }
                s.pop();
            }
        }
        return s.empty();
    }

    int main() {
        cout << correct_bracketing("(") << endl;  // false
        cout << correct_bracketing("()") << endl;  // true
        cout << correct_bracketing("(()())") << endl;  // true
        cout << correct_bracket