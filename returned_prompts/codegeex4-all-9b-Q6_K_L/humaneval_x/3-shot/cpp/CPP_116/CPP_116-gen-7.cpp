
Q1: Missing function signature.
Your function should be:
bool has_close_elements(const vector<float>& numbers, float threshold)

Q2: Missing function signature.
Your function should be:
vector<string> separate_paren_groups(const string& paren_string)

Q3: Missing function signature.
Your function should be:
float truncate_number(float number)

Q4: Missing function signature.
Your function should be:
vector<int> sort_array(const vector<int>& arr)

A1: The function has the correct signature.
However, your code is not correct. You are not correctly checking for the closest elements.
You should be doing something like:
for (i = 0; i < numbers.size(); ++i) {
    for (j = i + 1; j < numbers.size(); ++j) {
        if (abs(numbers[i] - numbers[j]) < threshold) {
            return true;
        }
    }
}

A2: The function has the correct signature.
However, your code is not correct. You are not correctly separating the groups.
You should be doing something like:
for (i = 0; i < paren_string.length(); ++i) {
    chr = paren_string[i];
    if (chr == '(') {
        level += 1;
        current_paren += chr;
    } else if (chr == ')') {
        level -= 1;
        current_paren += chr;
        if (level == 0) {
            all_parens.push_back(current_paren);
            current_paren = "";
        }
    }
}

A3: The function has the correct signature.
However, your code is not correct. You are not correctly truncating the number.
You should be doing something like:
return number - static_cast<int>(number);

A4: The function has the correct signature.
However, your code is not correct. You are not correctly sorting the array.
You should be doing something like:
sort(arr.begin(), arr.end(), [](int i, int j)