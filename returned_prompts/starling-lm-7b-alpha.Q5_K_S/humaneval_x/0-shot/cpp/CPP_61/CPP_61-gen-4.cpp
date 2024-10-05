    int n=brackets.size();
    int count=0;
    int i;
    for(i=0;i<n;i++)
    {
        if(brackets[i]=='(')
        {
            count++;
        }
        else if(brackets[i]==')')
        {
            count--;
        }
        if(count<0)
        {
            goto A;
        }
    }
    if(count!=0)
    {
        return false;
    }
    else
    {
        return true;
    }
}






ANSWER:
Yes
*/
#include <bits/stdc++.h>
using namespace std;

bool correct_bracketing(string brackets) {
    stack<char> s;
    for (auto c : brackets) {
        if (c == '(') {
            s.push(c);
        } else if (c == ')') {
            if (s.empty()) {
                return false;
            } else {
                s.pop();
            }
        }
    }
    return s.empty();
}


































































































































































































































