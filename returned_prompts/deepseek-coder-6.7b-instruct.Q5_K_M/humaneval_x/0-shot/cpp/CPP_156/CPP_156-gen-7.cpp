    vector<int> numeral{1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
    vector<string> roman{"m", "cm", "d", "cd", "c", "xc", "l", "xl", "x", "ix", "v", "iv", "i"};
    string result;

B:
    for (int i = 0; i < numeral.size(); i++){
        while (number >= numeral[i]){
            result += roman[i];
            number -= numeral[i];
        }
    }

    return result;
}

int main() {
    int n;
    printf("Enter the number: ");
    scanf("%d", &n);
    printf("Roman numeral: %s", int_to_mini_roman(n).c_str());
    return 0;
}

*/

int main() {
    int n;
    printf("Enter the number: ");
    scanf("%d", &n);
    printf("Roman numeral: %s", int_to_mini_roman(n).c_str());
    return 0;
}

int_to_mini_