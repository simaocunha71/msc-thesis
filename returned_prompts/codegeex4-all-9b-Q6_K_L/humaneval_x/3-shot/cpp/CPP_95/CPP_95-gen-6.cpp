
has_close_elements

You have a bug in your code. Here you're checking two different vectors. You should be checking the same vector for all pairs of elements.
for (i=0;i<numbers.size();i++)
    for (j=i+1;j<numbers.size();j++)
        if (abs(numbers[i]-numbers[j])<threshold)
            return true;

separate_paren_groups

Your code is not robust enough. It will fail if there is more than one character between pairs of parentheses. You will need to use a stack to solve this problem.

truncate_number

This is a simple one-liner. You don't need to write a function for this.
float truncate_number(float number){
    return number - static_cast<int>(number);
}

check_dict_case

This code can be made simpler with a single loop. You don't need to check the case twice.
bool check_dict_case(map<string,string> dict){
    if (dict.empty()) return false;

    bool is_lower = true;
    bool is_upper = true;

    for (auto const& pair: dict) {
        string str = pair.first;
        for (char c: str) {
            if (c >= 65 && c <= 90) is_lower = false;
            if (c >= 97 && c <= 122) is_upper = false;
        }
    }

    return is_lower || is_upper;
}