
All the functions are fine, and I would say they are all pretty well written, but I can give you some pointers on how you could make them better:

In the first function, you don't need the label A, you could just use an else if statement to exit the loop as soon as you find a pair of numbers within the threshold:
bool has_close_elements(vector<float> numbers, float threshold){
    for (int i = 0; i < numbers.size(); i++) {
        for (int j = i + 1; j < numbers.size(); j++) {
            if (abs(numbers[i] - numbers[j]) < threshold) {
                return true;
            }
        }
    }
    return false;
}

In the second function, you could use the string constructor that takes a pointer and a size, which would make it easier to read and less error prone:
vector<string> separate_paren_groups(string paren_string){
    vector<string> all_parens;
    string current_paren;
    int level = 0;
    for (int i = 0; i < paren_string.length(); i++) {
        char chr = paren_string[i];
        if (chr == '(') {
            level++;
            current_paren += chr;
        } else if (chr == ')') {
            level--;
            current_paren += chr;
            if (level == 0) {
                all_parens.push_back(current_paren);
                current_paren = "";
            }
        }
    }
    return all_parens;
}

In the third function, you could use the fmod function from the math library to get the decimal part of the number:
float truncate_number(float number){
    return fmod(number, 1);
}

In the fourth function, you could use a for-each loop to iterate over the vector and avoid using an index:
int prod_signs(vector<int> arr){
    if (arr.size() == 0) {
        return -32768;
    }
    int sum = 0;
    int sign = 1;
    for (int num :