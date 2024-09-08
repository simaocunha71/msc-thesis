#include <string>
using namespace std;
string string_sequence(int n) {
    string s = "";
    for(int i=0;i<=n;i++)
        s += to_string(i) + ' ';
    return s.substr(0,s.size()-1);
}

B:
#include <string>
using namespace std;
string string_sequence(int n) {
    string s = "";
    for(int i=0;i<=n;i++) {
        s += to_string(i);
        if (i != n)
            s += " ";
    }
    return s;
}

C:
#include <string>
using namespace std;
string string_sequence(int n) {
    string s = "";
    for(int i=0;i<=n;i++) {
        s += to_string(i) + " ";
    }
    return s.substr(0,s.size()-1);
}

D:
#include <string>
using namespace std;
string string_sequence(int n) {
    string s = "";
    for(int i=0;i<=n;i++) {
        s += to_string(i);
        if (i != n)
            s += " ";
    }
    return s;
}

E:
#include <string>
using namespace std;
string string_sequence(int n) {
    string s = "";
    for(int i=0;i<=n;i++)
        s += to_string(i);
    return s;
}

F:
#include <string>
using namespace std;
string string_sequence(int n) {
    string s = "";
    for(int i=0;i<=n;i++)
        s += to_string(i) + " ";
    return s.substr(0,s.size()-1);
}

G:
#include <string>
using namespace std;
string string_sequence(int n) {
    string s = "";
    for(int i=0;i<=n;i++) {
        s += to_string(i);
        if (i != n)
            s += " ";
    }
    return s.substr(0,s.size()-1);
}

H:
#include <string>
using namespace std;
string string_sequence(int n) {
    string s = "";
    for(int i=0;i<n;i++)
        s += to_string(i) + " ";
    return s.substr(0,s.size()-1);
}

I:
#include <string>
using namespace std;
string string_sequence(int n) {
    string s = "";
    for(int i=0;i<=n;i++)
        s += to_string(i) + " ";
    return s;
}

J:
#include <string>
using namespace std;
string string