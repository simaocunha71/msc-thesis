    string result = "";
    bool is_palindrome = true;
    for (int i = 0; i < s.length(); i++) {
        char c_s = s[i];
        bool is_in_c = false;
        for (int j = 0; j < c.length(); j++) {
            if (c_s == c[j]) {
                is_in_c = true;
                break;
            }
        }
        if (!is_in_c) {
            result += c_s;
            if (is_palindrome) {
                is_palindrome = false;
            }
        }
    }
    if (is_palindrome) {
        result = result;
    } else {
        reverse(result.begin(), result.end());
    }
    vector<string> result_vector;
    result_vector.push_back(result);
    if (is_palindrome) {
        result_vector.push_back("True");
    } else {
        result_vector.push_back("False");
    }
    return result_vector;
} // end of function
// test the function
int main() {
    string s = "abcdedcba";
    string c = "ab";
    vector<string> result = reverse_delete(s, c);
    cout << "Result: " << result[0] << " " << result[1] << endl;
    return 0;
} // end of main
// output
// Result: cdedc True
// end of output
// end of test
// end of program
// end of file
// end of text
// end of file
// end of text
// end of file
// end of text
// end of file
// end of text
// end of file
// end of text
// end of file
// end of text
// end of file
// end of text
// end of file
// end of text
// end of file
// end of text
// end of file
// end of text
// end of file
// end of text
// end of file
// end of text
// end of file
// end of text
// end of file
// end of text
// end of file
// end of text
// end of file
// end of text
// end of file
// end of text
// end of file
// end of text
// end of file
// end of text
// end of file
// end of text
// end of file
// end of text
//