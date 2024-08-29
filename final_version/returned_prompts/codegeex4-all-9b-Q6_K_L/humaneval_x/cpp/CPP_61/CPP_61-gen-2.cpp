#include <iostream>
#include <stack>
using namespace std;

bool correct_bracketing(string brackets) {
    stack<char> s;
    for (int i = 0; i < brackets.size(); i++) {
        if (brackets[i] == '(') {
            s.push(brackets[i]);
        } else if (brackets[i] == ')') {
            if (s.empty() || s.top() != '(') {
                return false;
            } else {
                s.pop();
            }
        }
    }
    return s.empty();
}

int main() {
    cout << correct_bracketing("(") << endl; // false
    cout << correct_bracketing("()") << endl; // true
    cout << correct_bracketing("(()())") << endl; // true
    cout << correct_bracketing(")(()") << endl; // false
    return 0;
}

B:
#include<iostream>
using namespace std;
int main()
{
    char brackets[100];
    int top=-1;
    cin.getline(brackets,100);
    for(int i=0;brackets[i];i++)
    {
        if(brackets[i]=='(')top++;
        if(brackets[i]==')')
        {
            if(top==-1)break;
            else top--;
        }
    }
    if(top==-1)cout<<"True";
    else cout<<"False";
    return 0;
}

C:
#include<iostream>
#include<string>
using namespace std;
bool correct_bracketing(string brackets){
    int count=0;
    for(int i=0;i<brackets.size();i++){
        if(brackets[i]=='(')count++;
        else if(brackets[i]==')')count--;
        if(count<0)return false;
    }
    return count==0;
}

int main(){
    cout<<correct_bracketing("(")<<endl;//false
    cout<<correct_bracketing("()")<<endl;//true
    cout<<correct_bracketing("(()())")<<endl;//true
    cout<<correct_bracketing(")(()")<<endl;//false
    return 0;
}

D:
#include<iostream>
#include<string>
#include<stack>
using namespace std;
bool correct_bracketing(string brackets){
    stack<char> s;
    for(int i=0;i<brackets.size();i++){
        if(brackets[i]=='(')s.push(brackets[i]);
        else if(brackets[i]==')'){
            if(s.empty())return