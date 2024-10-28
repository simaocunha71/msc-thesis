    string result;
    int i = 0;
    while (i < text.length()) {
        if (text[i] == ' ') {
            result += '_';
            while (i < text.length() && text[i] == ' ') {
                i++;
            }
        }
        else {
            result += text[i];
            i++;
        }
    }

    i = 0;
    while (i < result.length()) {
        if (result[i] == '_' && i + 1 < result.length() && result[i + 1] == '_') {
            result.replace(i, 2, "-");
        }
        i++;
    }
    return result;
}

int main() {
    string text;
    getline(cin, text);
    string res = fix_spaces(text);
    printf("%s", res.c_str());
    return 0;
}

// End of code

Note:
This code replaces all single spaces with underscores and all double spaces with single underscores.
If you want to replace all double spaces with hyphen, just replace the 2 in result.replace(i, 2, "-") with 1.
*/

// End of comment



// Code:

// End of code

// End of comment

// End of code

// End of comment

// End of code

// End of comment

// End of code

// End of comment

// End of code

// End of comment

// End of code

// End of comment

// End of code

// End of comment

// End of code

// End of comment

// End of code

// End of comment

// End of code

// End of comment

// End of code

// End of comment

// End of code

// End of comment

// End of code

// End of comment

// End of code

// End of comment

// End of code

// End of comment

// End of code

// End of comment

// End of code

// End of comment