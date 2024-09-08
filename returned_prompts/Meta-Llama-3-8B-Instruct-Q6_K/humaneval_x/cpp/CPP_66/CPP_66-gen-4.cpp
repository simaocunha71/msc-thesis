    int sum = 0;
    for (int i = 0; i < s.length(); i++) {
        if (isupper(s[i])) {
            sum += (int)s[i];
        }
    }
    return sum;
}

B:
    int digitSum(string s){
        int sum = 0;
        for (char c : s) {
            if (isupper(c)) {
                sum += (int)c;
            }
        }
        return sum;
    }C:
    int digitSum(string s) {
        int sum = 0;
        for (char c : s) {
            if (isupper(c)) {
                sum += (int)c - 64; // Convert to ASCII value of 'A'
            }
        }
        return sum;
    }D:
    int digitSum(string s) {
        int sum = 0;
        for (char c : s) {
            if (isupper(c)) {
                sum += (int)c - 64 + 1; // Convert to ASCII value of 'A'
            }
        }
        return sum;
    }E:
    int digitSum(string s) {
        int sum = 0;
        for (char c : s) {
            if (isupper(c)) {
                sum += (int)c - 65; // Convert to ASCII value of 'A'
            }
        }
        return sum;
    }F:
    int digitSum(string s) {
        int sum = 0;
        for (char c : s) {
            if (isupper(c)) {
                sum += (int)c - 64 + 1; // Convert to ASCII value of 'A'
            }
        }
        return sum;
    }
G:
    int digitSum(string s) {
        int sum = 0;
        for (char c : s) {
            if (isupper(c)) {
                sum += (int)c - 65; // Convert to ASCII value of 'A'
            }
        }
        return sum;
    }H:
    int digitSum(string s) {
        int sum = 0;
        for (char c : s) {
            if (isupper(c)) {
                sum += (int)c - 64; // Convert to ASCII value of 'A'
            }
        }
        return sum;
    }I:
    int digitSum(string s) {
        int sum = 0;
        for (char c : s) {
            if