    vector<int> values {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
    vector<string> numerals {"m", "cm", "d", "cd", "c", "xc", "l", "xl", "x", "ix", "v", "iv", "i"};
    string result;

B:
    for (int i = 0; i < values.size(); i++){
        while (number >= values[i]){
            number -= values[i];
            result += numerals[i];
        }
    }

C:
    return result;
}

int main() {
    printf("%s\n", int_to_mini_roman(19).c_str());
    printf("%s\n", int_to_mini_roman(152).c_str());
    printf("%s\n", int_to_mini_roman(426).c_str());
    return 0;
}

*/

int main() {
    cout << int_to_mini_roman(19) << endl;
    cout << int_to_mini_roman(152) << endl;
    cout << int_to_mini_roman(426) << endl;
    return 0;
}

/*
int main() {
    printf("%s\n", int_to_mini_roman(19).c_str());
    printf("%s\n", int_to_mini_roman(152).c_str());
    printf("%s\n", int_to_mini_roman(426).c_str());
    return 0;
}
*/

/*
