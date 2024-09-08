    int i = 0, j = text.size() - 1;
    while (i < j) {
        if (text[i] != text[j]) {
            return false;
        }
        i++;
        j--;
    }
    return true;
}

int main() {
    printf("%d\n", is_palindrome("")); // prints 1
    printf("%d\n", is_palindrome("aba")); // prints 1
    printf("%d\n", is_palindrome("aaaaa")); // prints 1
    printf("%d\n", is_palindrome("zbcd")); // prints 0
    return 0;
}
