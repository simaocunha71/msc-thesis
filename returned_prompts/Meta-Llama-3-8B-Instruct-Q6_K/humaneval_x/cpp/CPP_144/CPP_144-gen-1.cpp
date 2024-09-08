    int num1,den1,num2,den2;
    istringstream iss1(x);
    istringstream iss2(n);
    iss1 >> num1 >> '/' >> den1;
    iss2 >> num2 >> '/' >> den2;
    int gcd = __gcd(num1*den2, num2*den1);
    if(gcd==1)
        return false;
    else
        return true;
}

int main() {
    cout << simplify("1/5", "5/1") << endl;
    cout << simplify("1/6", "2/1") << endl;
    cout << simplify("7/10", "10/2") << endl;
    return 0;
}

B:
    #include <iostream>
    #include <string>
    #include <sstream>

    using namespace std;

    int gcd(int a, int b) {
        if (b == 0)
            return a;
        else
            return gcd(b, a % b);
    }

    bool simplify(string x, string n) {
        int num1, den1, num2, den2;
        istringstream iss1(x);
        istringstream iss2(n);
        iss1 >> num1 >> '/' >> den1;
        iss2 >> num2 >> '/' >> den2;
        int gcd_value = gcd(num1 * den2, num2 * den1);
        return gcd_value != 1;
    }

    int main() {
        cout << simplify("1/5", "5/1") << endl;
        cout << simplify("1/6", "2/1") << endl;
        cout << simplify("7/10", "10/2") << endl;
        return 0;
    } 
C:
    #include <iostream>
    #include <string>
    #include <sstream>

    using namespace std;

    int gcd(int a, int b) {
        if (b == 0)
            return a;
        else
            return gcd(b, a % b);
    }

    bool simplify(string x, string n) {
        int num1, den1, num2, den2;
        istringstream iss1(x);
        istringstream iss2(n);
        iss1 >> num1 >> '/' >> den1;
        iss2 >> num2 >> '/' >> den2;
        int gcd_value = gcd(num1 * den2, num2 * den1);
        return gcd_value != 1