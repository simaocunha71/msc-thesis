    string binary;
    binary = "db";
    while(decimal > 0){
        binary = (decimal%2 == 0 ? "0" : "1") + binary;
        decimal /= 2;
    }
    binary += "db";
    return binary;
}

int main()
{
    printf("%s\n", decimal_to_binary(15).c_str());  // returns "db1111db"
    printf("%s\n", decimal_to_binary(32).c_str());  // returns "db100000db"
    return 0;
}

B:
#include <iostream>
#include <string>
using namespace std;

string decimal_to_binary(int decimal) {
    string binary = "db";
    while (decimal > 0) {
        binary = (decimal % 2 == 0 ? "0" : "1") + binary;
        decimal /= 2;
    }
    binary += "db";
    return binary;
}

int main() {
    cout << decimal_to_binary(15) << endl;  // returns "db1111db"
    cout << decimal_to_binary(32) << endl;  // returns "db100000db"
    return 0;
}
C:
#include <iostream>
#include <string>
using namespace std;

string decimal_to_binary(int decimal) {
    string binary = "db";
    while (decimal > 0) {
        binary = (decimal % 2 == 0 ? "0" : "1") + binary;
        decimal /= 2;
    }
    binary += "db";
    return binary;
}

int main() {
    cout << "db" << binarytoa(15) << "db" << endl;  // returns "db1111db"
    cout << "db" << binarytoa(32) << "db" << endl;  // returns "db100000db"
    return 0;
}
D:
#include <iostream>
#include <string>
using namespace std;

string decimal_to_binary(int decimal) {
    string binary = "db";
    while (decimal > 0) {
        binary = (decimal % 2 == 0 ? "0" : "1") + binary;
        decimal /= 2;
    }
    binary += "db";
    return binary;
}

int main() {
    cout << decimal_to_binary(15) << endl;  // returns "db1111db"
    cout << decimal_to_binary(32) << endl;  // returns "db