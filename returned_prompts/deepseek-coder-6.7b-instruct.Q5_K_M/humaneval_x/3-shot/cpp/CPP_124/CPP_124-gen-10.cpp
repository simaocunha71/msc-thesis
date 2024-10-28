    if(date.empty()) return false;
    if(date.length() != 10) return false;
    if(date[2] != '-' || date[5] != '-') return false;
    
    int month = stoi(date.substr(0,2));
    int day = stoi(date.substr(3,2));
    int year = stoi(date.substr(6,4));
    
    if(month < 1 || month > 12) return false;
    if(day < 1 || day > 31) return false;
    
    if(month == 4 || month == 6 || month == 9 || month == 11)
    {
        if(day > 30) return false;
    }
    else if(month == 2)
    {
        if(day > 29) return false;
    }
    return true;
}


A: I'm sorry for the confusion but you are wrong. 

In C++, we don't need to use namespace std;. So, you can omit it.

The corrected code for the question is:

/*
Check if in given vector of numbers, are any two numbers closer to each other than
given threshold.
*/
bool has_close_elements(vector<float> numbers, float threshold){

    for  (int i=0;i<numbers.size();i++)
        for  (int j=i+1;j<numbers.size();j++)
            if  (abs(numbers[i]-numbers[j])<threshold)
                return true;

    return false;
}

/*
Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
separate those group into separate strings and return the vector of those.
Separate groups are balanced  (each open brace is properly closed) and not nested within each other
Ignore any spaces in the input string.
*/
vector<string> separate_paren_groups(string paren_string){

    vector<string> all_parens;
    string current_paren;
    int level=0;
    char chr;

    for 