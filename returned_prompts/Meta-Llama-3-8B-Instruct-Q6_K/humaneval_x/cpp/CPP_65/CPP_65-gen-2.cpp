    string s = to_string(x);
    int n = s.length();
    shift = shift % n;
    if(shift == 0) return s;
    return s.substr(shift) + s.substr(0, shift);
}
int main(){
    printf("%s\n",circular_shift(12,1).c_str());
    printf("%s\n",circular_shift(12,2).c_str());
    return 0;
}
B:
    string circular_shift(int x, int shift) {
        string s = to_string(x);
        int n = s.length();
        shift = shift % n;
        if(shift == 0) return s;
        string left = s.substr(0, n - shift);
        string right = s.substr(n - shift, shift);
        return right + left;
    }
    int main() {
        printf("%s\n", circular_shift(12, 1).c_str());
        printf("%s\n", circular_shift(12, 2).c_str());
        return 0;
    }
C:
    string circular_shift(int x, int shift) {
        string s = to_string(x);
        int n = s.length();
        shift = shift % n;
        if(shift == 0) return s;
        char* p = new char[n+1];
        strcpy(p,s.c_str());
        for(int i = 0;i < n-shift;i++) p[i+shift] = p[i];
        p[i+shift] = '\0';
        return string(p);
    }
    int main() {
        printf("%s\n", circular_shift(12, 1).c_str());
        printf("%s\n", circular_shift(12, 2).c_str());
        return 0;
    }
D:
    string circular_shift(int x, int shift) {
        string s = to_string(x);
        int n = s.length();
        shift = shift % n;
        if(shift == 0) return s;
        string left = s.substr(0, n - shift);
        string right = s.substr(n - shift, shift);
        return right + left;
    }
    int main() {
        printf("%s\n", circular_shift(12, 1).c_str());
        printf("%s\n", circular_shift(12, 2).c_str());
        return 0;
    }
E:
    string circular_shift(int x, int shift) {
        string s = to_string(x);
        int n = s