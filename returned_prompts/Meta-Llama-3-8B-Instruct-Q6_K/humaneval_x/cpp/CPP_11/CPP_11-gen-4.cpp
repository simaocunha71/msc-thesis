    int i, length;
    length = a.length();
    string result;
    for(i=0; i<length; i++)
    {
        if(a[i] == b[i])
        {
            result += '0';
        }
        else
        {
            result += '1';
        }
    }
    return result;
}
int main()
{
    string a,b;
    cout<<"Enter string a : ";
    cin>>a;
    cout<<"Enter string b : ";
    cin>>b;
    string_xor(a,b);
    return 0;
}
B:
#include<string>
using namespace std;

string string_xor(string a, string b) {
    string result;
    for (int i = 0; i < a.size(); i++) {
        result += (a[i] - '0' ^ b[i] - '0') + '0';
    }
    return result;
}

int main() {
    string a, b;
    cout << "Enter string a : ";
    cin >> a;
    cout << "Enter string b : ";
    cin >> b;
    cout << "XOR result: " << string_xor(a, b) << endl;
    return 0;
}
C:
#include<string>
using namespace std;

string string_xor(string a, string b) {
    string result;
    for (int i = 0; i < a.size(); i++) {
        result += (a[i] == b[i]) ? '0' : '1';
    }
    return result;
}

int main() {
    string a, b;
    cout << "Enter string a : ";
    cin >> a;
    cout << "Enter string b : ";
    cin >> b;
    cout << "XOR result: " << string_xor(a, b) << endl;
    return 0;
}
D:
#include<string>
using namespace std;

string string_xor(string a, string b) {
    string result;
    for (int i = 0; i < a.size(); i++) {
        result += (a[i] ^ b[i]);
    }
    return result;
}

int main() {
    string a, b;
    cout << "Enter string a : ";
    cin >> a;
    cout << "Enter string b : ";
    cin >> b;
    cout << "XOR result: " << string_xor(a, b) << endl;
    return 0;
}
E:
#include<string>
using namespace std;

string string_xor(string