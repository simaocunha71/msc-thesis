
has_close_elements
Your algorithm has a time complexity of O(n^2). You can improve it to O(n) by sorting the vector and comparing it with the adjacent elements. Here is the modified version of your function:

bool has_close_elements(vector<float> numbers, float threshold){
    sort(numbers.begin(), numbers.end());
    for(int i = 0; i < numbers.size() - 1; ++i){
        if(numbers[i + 1] - numbers[i] < threshold)
            return true;
    }
    return false;
}

separate_paren_groups
Your algorithm has a time complexity of O(n). However, you should also check if the parentheses are balanced in your solution. Otherwise, it may return invalid results. Here is the modified version of your function:

vector<string> separate_paren_groups(string paren_string){
    vector<string> all_parens;
    string current_paren;
    int level = 0;
    char chr;
    int i;
    for(i = 0; i < paren_string.length(); ++i){
        chr = paren_string[i];
        if(chr == '('){
            level += 1;
            current_paren += chr;
        }
        if(chr == ')'){
            level -= 1;
            current_paren += chr;
            if(level == 0){
                all_parens.push_back(current_paren);
                current_paren = "";
            }
        }
    }
    if(level != 0)
        throw invalid_argument("Unbalanced parentheses");
    return all_parens;
}

truncate_number
Your algorithm has a time complexity of O(1). You can return the decimal part of the number directly.

float truncate_number(float number){
    return number - (int)number;
}

prod_signs
Your algorithm has a time complexity of O(n). You can return the product of the signs and the sum of the magnitudes directly.

int prod_signs(vector<int> arr){
    if(arr.empty())
        return -32768;
    int prod_sign = 1;
    int sum_magnitudes = 0;
    for(int i = 0; i < arr.size();