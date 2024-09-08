    string s = to_string(x);
    int n = s.length();
    shift = shift % n;
    if(shift == 0) return s;
    return s.substr(shift) + s.substr(0,shift);

}
int main() {
    int x = 12, shift = 1;
    string result = circular_shift(x, shift);
    printf("%s\n", result.c_str());
    return 0;
}

B:
    #include <iostream>
    #include <string>
    #include <sstream>

    using namespace std;

    string circular_shift(int x, int shift) {
        stringstream ss;
        ss << x;
        string str = ss.str();
        int n = str.length();
        shift = shift % n;
        if(shift == 0) return str;
        return str.substr(shift) + str.substr(0, shift);
    }

    int main() {
        int x = 12, shift = 1;
        string result = circular_shift(x, shift);
        cout << result << endl;
        return 0;
    }

C:
    #include <iostream>
    #include <string>
    #include <vector>

    using namespace std;

    string circular_shift(int x, int shift) {
        string s = to_string(x);
        int n = s.length();
        shift = shift % n;
        if(shift == 0) return s;
        vector<char> v(s.begin(), s.end());
        reverse(v.begin() + shift, v.end());
        reverse(v.begin(), v.end());
        return string(v.begin(), v.end());
    }

    int main() {
        int x = 12, shift = 1;
        string result = circular_shift(x, shift);
        cout << result << endl;
        return 0;
    }

D:
    #include <iostream>
    #include <string>
    #include <vector>

    using namespace std;

    string circular_shift(int x, int shift) {
        string s = to_string(x);
        int n = s.length();
        shift = shift % n;
        if(shift == 0) return s;
        string first = s.substr(shift);
        string second = s.substr(0, shift);
        return first + second;
    }

    int main() {
        int x = 12, shift = 1;
        string result = circular_shift(x, shift);
        cout << result << endl;
        return 0;
    }

Answer: D:
