    int i, count=0;
    for(i=0; i<brackets.length(); i++)
    {
        if(brackets[i] == '(')
            count++;
        if(brackets[i] == ')')
            count--;
        if(count < 0)
            return false;
    }
    return (count == 0);
} //end of function
//test cases
cout << correct_bracketing("(") << endl; // expected output: false
cout << correct_bracketing("()") << endl; // expected output: true
cout << correct_bracketing("(()())") << endl; // expected output: true
cout << correct_bracketing(")(()") << endl; // expected output: false
//end of test cases
//end of program
//end of function
//end of function

