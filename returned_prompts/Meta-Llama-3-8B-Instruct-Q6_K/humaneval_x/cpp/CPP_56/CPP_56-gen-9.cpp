    int count = 0;
    for (int i = 0; i < brackets.length(); i++) {
        if (brackets[i] == '<') {
            count++;
        } else if (brackets[i] == '>') {
            if (count == 0) {
                return false;
            }
            count--;
        }
    }
    if (count != 0) {
        return false;
    }
    return true;
}

int main() {
    printf("%d\n", correct_bracketing("<")); // 0
    printf("%d\n", correct_bracketing("<>")); // 1
    printf("%d\n", correct_bracketing("<<><>>")); // 1
    printf("%d\n", correct_bracketing("><<>")); // 0
    return 0;
}
