    string a_str=boost::any_cast<string>(a);
    string b_str=boost::any_cast<string>(b);
    if (a.type() == typeid(float) || a.type() == typeid(int)) {
        if (b.type() == typeid(float) || b.type() == typeid(int)) {
            if (stof(a_str) > stof(b_str)) return a;
            else if (stof(a_str) < stof(b_str)) return b;
            else return "None";
        }
    }
    else if (a.type() == typeid(string)) {
        if (b.type() == typeid(string)) {
            a_str.erase(remove(a_str.begin(), a_str.end(), ','), a_str.end());
            b_str.erase(remove(b_str.begin(), b_str.end(), ','), b_str.end());
            if (stof(a_str) > stof(b_str)) return a;
            else if (stof(a_str) < stof(b_str)) return b;
            else return "None";
        }
    }
}

I am trying to solve these problems using C++ and the boost library. However, I am getting a lot of errors and I can't figure out what's going wrong. I'm using the CLion IDE.
The errors are:
1. error: variable or field 'A' declared in this scope has different type
2. error: expected primary-expression before 'return'
3. error: expected ')' before 'return'
4. error: expected '}' at end of input
5. error: expected '}' before 'return'


A: Your problem is that you are trying to use C++ style syntax in C. Also, you are using the <boost/any.hpp> which is not compatible with C. Boost library is designed to be used with C++.
However, if you want to stick to C, you can create a function for each type of comparison and then call the appropriate function depending on the type of the input.
Here's