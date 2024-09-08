    int num = x;  // store the original number
    int n = 0;    // number of digits
    while(num > 0) {
        num /= 10;
        n++;
    }
    shift = shift % n;  // if shift > number of digits, shift = shift % n
    if(shift == 0) return to_string(x);  // if shift = 0, return the original number
    int res = 0;
    num = x;  // restore the original number
    int i = 0;
    while(num > 0) {
        res = res * 10 + (num % 10);  // store the last digit
        num /= 10;
        if(i >= shift) {  // if the current digit is shifted, break the loop
            break;
        }
        i++;
    }
    while(num > 0) {
        res = res * 10 + (num % 10);  // store the remaining digits
        num /= 10;
    }
    return to_string(res);
}
int main()
{
    cout<<circular_shift(12,1)<<endl; //output:21
    cout<<circular_shift(12,2)<<endl; //output:12
    return 0;
}

B:
string circular_shift(int x, int shift) {
    string s = to_string(x);
    shift = shift % s.size();
    return s.substr(shift) + s.substr(0, shift);
}
int main() {
    cout << circular_shift(12, 1) << endl; // output:21
    cout << circular_shift(12, 2) << endl; // output:12
    return 0;
}
C:
string circular_shift(int x, int shift) {
    string s = to_string(x);
    shift = shift % s.size();
    if(shift == 0) return s;
    return s.substr(shift) + s.substr(0, shift);
}
int main() {
    cout << circular_shift(12, 1) << endl; // output:21
    cout << circular_shift(12, 2) << endl; // output:12
    return 0;
}
D:
string circular_shift(int x, int shift) {
    string s = to_string(x);
    shift = shift % s.size();
    string left, right;
    left = s.substr(0, shift);
    right =