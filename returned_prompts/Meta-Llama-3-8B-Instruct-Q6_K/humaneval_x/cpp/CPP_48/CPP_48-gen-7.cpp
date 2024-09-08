    int i = 0;
    int j = text.length() - 1;
    while(i <= j){
        if(text[i] != text[j])
            return false;
        i++;
        j--;
    }
    return true;
}
int main() {
    string str;
    cout << "Enter a string: ";
    getline(cin, str);
    if (is_palindrome(str))
        cout << str << " is a palindrome.\n";
    else
        cout << str << " is not a palindrome.\n";
    return 0;
}

