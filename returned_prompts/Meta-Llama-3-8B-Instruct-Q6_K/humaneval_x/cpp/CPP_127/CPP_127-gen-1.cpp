    int start1 = interval1[0];
    int end1 = interval1[1];
    int start2 = interval2[0];
    int end2 = interval2[1];

    int intersectionStart = max(start1, start2);
    int intersectionEnd = min(end1, end2);

    if (intersectionStart <= intersectionEnd) {
        int intersectionLength = intersectionEnd - intersectionStart + 1;
        for (int i = 2; i * i <= intersectionLength; i++) {
            if (intersectionLength % i == 0) {
                return "NO";
            }
        }
        return "YES";
    } else {
        return "NO";
    }
}

B:
    int start1 = interval1[0];
    int end1 = interval1[1];
    int start2 = interval2[0];
    int end2 = interval2[1];

    int intersectionStart = max(start1, start2);
    int intersectionEnd = min(end1, end2);

    if (intersectionStart <= intersectionEnd) {
        int intersectionLength = intersectionEnd - intersectionStart + 1;
        if (isPrime(intersectionLength)) {
            return "YES";
        } else {
            return "NO";
        }
    } else {
        return "NO";
    }
}

C:
    int start1 = interval1[0];
    int end1 = interval1[1];
    int start2 = interval2[0];
    int end2 = interval2[1];

    int intersectionStart = max(start1, start2);
    int intersectionEnd = min(end1, end2);

    if (intersectionStart <= intersectionEnd) {
        int intersectionLength = intersectionEnd - intersectionStart + 1;
        return isPrime(intersectionLength) ? "YES" : "NO";
    } else {
        return "NO";
    }
}
int isPrime(int n) {
    if (n <= 1) return 0;
    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0) {
            return 0;
        }
    }
    return 1;
}

D:
    int start1 = interval1[0];
    int end1 = interval1[1];
    int start2 = interval2[0];
    int end2 = interval2[1];

    int intersectionStart = max(start1, start2);
    int intersectionEnd