
Your code is missing the main function for testing. Add the following code to test the functions you provided:
int main() {
    vector<float> numbers1 = {1.0, 2.0, 3.0};
    vector<float> numbers2 = {1.0, 2.8, 3.0, 4.0, 5.0, 2.0};
    float threshold = 0.5;
    bool result1 = has_close_elements(numbers1, threshold);
    bool result2 = has_close_elements(numbers2, threshold);
    printf("Result 1: %d\n", result1);
    printf("Result 2: %d\n", result2);

    string paren_string = "( ) (( )) (( )( ))";
    vector<string> paren_groups = separate_paren_groups(paren_string);
    for (string group : paren_groups) {
        printf("Group: %s\n", group.c_str());
    }

    float number = 3.5;
    float result3 = truncate_number(number);
    printf("Result 3: %f\n", result3);

    int x = 12;
    int y = 15;
    int result4 = choose_num(x, y);
    printf("Result 4: %d\n", result4);

    return 0;
}

Make sure to include the necessary headers for each function.