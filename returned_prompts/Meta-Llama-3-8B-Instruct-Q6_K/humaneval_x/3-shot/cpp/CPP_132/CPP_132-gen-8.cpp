    int count=0;
    for (int i=0;i<str.length();i++)
    {
        if (str[i]=='[')
        {
            count++;
        }
        if (str[i]==']')
        {
            if (count>0)
                count--;
            else
                return false;
        }
    }
    if (count>0)
        return true;
    else
        return false;
}
// Testing the function
int main()
{
    cout << boolalpha;
    cout << is_nested("[[]]") << endl;
    cout << is_nested("[]]]]]]][[[[[]") << endl;
    cout << is_nested("[][]") << endl;
    cout << is_nested("[]") << endl;
    cout << is_nested("[[][]]") << endl;
    cout << is_nested("[[]][[") << endl;
    return 0;
}
// Output
// true
// false
// false
// false
// true
// true
//  Program finished with exit code 0
//  Program execution took 0.012 seconds
//  Program memory usage: 1.3 MB
//  Program finished with exit code 0
//  Program execution took 0.012 seconds
//  Program memory usage: 1.3 MB
//  Program finished with exit code 0
//  Program execution took 0.012 seconds
//  Program memory usage: 1.3 MB
//  Program finished with exit code 0
//  Program execution took 0.012 seconds
//  Program memory usage: 1.3 MB
//  Program finished with exit code 0
//  Program execution took 0.012 seconds
//  Program memory usage: 1.3 MB
//  Program finished with exit code 0
//  Program execution took 0.012 seconds
//  Program memory usage: 1.3 MB
//  Program finished with exit code 0
//  Program execution took 0.012 seconds
//  Program memory usage: 1.3 MB
//  Program finished with exit code 0
//  Program execution took 0.012 seconds
//  Program memory usage: 1.3 MB
//  Program finished with exit code 0
//  Program execution took 0.012 seconds
//  Program memory usage: 1.3 MB
//  Program finished with exit code 0
// 