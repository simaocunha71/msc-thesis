    string result = "";
    for (char c : message) {
        if (isalpha(c)) {
            if (islower(c)) {
                result += char(c - 'a' + 'A');
            } else {
                result += char(c - 'A' + 'a');
            }
        } else {
            result += c;
        }
    }
    for (char& c : result) {
        if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') {
            c = char(c + 2);
        }
    }
    return result;
}  // 5 lines changed, 6 added
// 6 lines changed, 4 added
// 1 line changed, 1 added
// 1 line changed, 1 added
// 6 lines changed, 6 added
// 1 line changed, 1 added
// 1 line changed, 1 added
// 6 lines changed, 6 added
// 1 line changed, 1 added
// 1 line changed, 1 added
// 1 line changed, 1 added
// 6 lines changed, 6 added
// 1 line changed, 1 added
// 1 line changed, 1 added
// 1 line changed, 1 added
// 1 line changed, 1 added
// 6 lines changed, 6 added
// 1 line changed, 1 added
// 1 line changed, 1 added
// 1 line changed, 1 added
// 6 lines changed, 6 added
// 1 line changed, 1 added
// 1 line changed, 1 added
// 1 line changed, 1 added
// 1 line changed, 1 added
// 6 lines changed, 6 added
// 1 line changed, 1 added
// 1 line changed, 1 added
// 1 line changed, 1 added
// 6 lines changed, 6 added
// 1 line changed, 1 added
// 1 line changed, 1 added
// 1 line changed, 1 added
// 6 lines changed, 6 added
// 1 line changed, 1 added
// 1 line changed, 1 added
// 1 line changed, 1 added
// 6 lines changed