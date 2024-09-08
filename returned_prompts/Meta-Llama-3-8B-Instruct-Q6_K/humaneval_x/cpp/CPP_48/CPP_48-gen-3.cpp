    int i = 0, j = text.length() - 1;
    while (i < j) {
        if (text[i] != text[j])
            return false;
        i++;
        j--;
    }
    return true;
}

int main() {
    string text;
    cout << "Enter a string: ";
    cin >> text;
    if(is_palindrome(text))
        cout << "The string is a palindrome" << endl;
    else
        cout << "The string is not a palindrome" << endl;
    return 0;
}

