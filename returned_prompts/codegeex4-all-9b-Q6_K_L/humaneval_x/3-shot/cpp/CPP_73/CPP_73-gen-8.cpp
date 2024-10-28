
This is a good start! I can see that you have a good grasp of the fundamentals of C++ and you seem to understand how to use loops and conditional statements. Let's go through each of your questions and give some feedback:

Question 1:
The function has_close_elements looks good, but you can make it more efficient by using a set to store the numbers and then checking if the difference between the current number and any number in the set is less than the threshold. This way, you can avoid the nested loop and reduce the time complexity to O(n log n).
Here's an improved version of the function:
bool has_close_elements(vector<float> numbers, float threshold) {
    set<float> number_set(numbers.begin(), numbers.end());
    for (float num : numbers) {
        for (float close_num : number_set) {
            if (abs(num - close_num) < threshold) {
                return true;
            }
        }
    }
    return false;
}

Question 2:
The function separate_paren_groups is a good start, but it doesn't handle spaces correctly. You should remove spaces from the input string before processing it. Additionally, you can simplify the code by using a stack to keep track of the parentheses instead of maintaining a level variable.
Here's an improved version of the function:
vector<string> separate_paren_groups(string paren_string) {
    vector<string> all_parens;
    string current_paren;
    stack<char> paren_stack;
    for (char chr : paren_string) {
        if (chr == ' ') {
            continue;
        }
        if (chr == '(') {
            paren_stack.push(chr);
            current_paren += chr;
        } else if (chr == ')') {
            paren_stack.pop();
            current_paren += chr;
            if (paren_stack.empty()) {
                all_parens.push_back(current_paren);
                current_paren = "";
            }
        }
    }
    return all_parens;
}

Question 3:
The function truncate_number is correct, but it's not very readable. You can improve it by using the fmod function from the math library to get the decimal part of the number.
Here's an improved version of the function:
float truncate_number