    vector<string> nums = { "i", "ii", "iii", "iv", "v", "vi", "vii", "viii", "ix" };
    vector<string> tens = { "x", "xx", "xx", "xc", "c", "xc", "l", "l", "xl", "lx", "lx", "xc" };
    vector<string> hundreds = { "c", "cc", "cc", "ccc", "d", "d", "dc", "dcc", "dccc", "cm" };
    vector<string> thousands = { "m", "mm", "mmm" };
    vector<int> ints = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000 };
    string ret = "";

    for (int i = 0; i < ints.size(); i++) {
        int n = number / ints[i];
        if (n > 0) {
            ret += tens[i];
            n--;
            if (n > 0) {
                ret += tens[i];
                n--;
                if (n > 0) {
                    ret += tens[i];
                    n--;
                }
            }
        }
        number %= ints[i];
    }
    return ret;
}

int main() {
    printf("%s\n", int_to_mini_romank(19).c_str());
    printf("%s\n", int_to_mini_romank(152).c_str());
    printf("%s\n", int_to_mini_romank(426).c_str());
    printf("%s\n", int_to_mini