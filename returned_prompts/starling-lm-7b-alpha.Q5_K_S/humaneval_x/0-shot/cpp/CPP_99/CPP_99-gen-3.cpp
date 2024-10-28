    int result = 0;
    int len = value.length();
    int i = 0;
    int j = 0;
    int x = 0;
    int y = 0;
    for(i = 0; i < len; i++) {
        if (value[i] == '.') {
            j = i;
            break;
        }
    }
    for (x = 0; x < j; x++) {
        result *= 10;
        result += value[x] - '0';
    }
    for (y = 0; y < len - j - 1; y++) {
        result *= 10;
        result += value[len - y - 1] - '0';
    }
    if (x > y) {
        result += 1;
    } else {
        result -= 1;
    }
    return result;
}

int main() {
    string value = "10";
    int result = closest_integer(value);
    printf("%d\n", result);
    return 0;
}

*/






















































































































































































































































