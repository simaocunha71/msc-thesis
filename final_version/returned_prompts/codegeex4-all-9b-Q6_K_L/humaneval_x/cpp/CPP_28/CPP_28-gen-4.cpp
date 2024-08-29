#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main() {
    vector<string> strings = {"a", "b", "c"};
    string concatenated = "";
    for (auto& s : strings) {
        concatenated += s;
    }
    cout << concatenated << endl;
    return 0;
}

C:
#include <iostream>
#include <vector>
#include <string>
using namespace std;

string concatenate(vector<string> strings) {
    string result = "";
    for (auto& str : strings) {
        result += str;
    }
    return result;
}

int main() {
    vector<string> strings = {"a", "b", "c"};
    string concatenated = concatenate(strings);
    cout << concatenated << endl;
    return 0;
}

D:
#include <iostream>
#include <vector>
#include <string>
using namespace std;

string concatenate(vector<string> strings) {
    string result = "";
    for (auto str : strings) {
        result += str;
    }
    return result;
}

int main() {
    vector<string> strings = {"a", "b", "c"};
    string concatenated = concatenate(strings);
    cout << concatenated << endl;
    return 0;
}

E:
#include <iostream>
#include <vector>
#include <string>
using namespace std;

string concatenate(vector<string> strings) {
    string result = "";
    for (auto str : strings) {
        result += str;
    }
    return result;
}

int main() {
    vector<string> strings = {"a", "b", "c"};
    cout << concatenate(strings) << endl;
    return 0;
}

F:
#include <iostream>
#include <vector>
#include <string>
using namespace std;

string concatenate(vector<string> strings) {
    string result = "";
    for (auto str : strings) {
        result.append(str);
    }
    return result;
}

int main() {
    vector<string> strings = {"a", "b", "c"};
    cout << concatenate(strings) << endl;
    return 0;
}

G:
#include <iostream>
#include <vector>
#include <string>
using namespace std;

string concatenate(vector<string> strings) {
    string result = "";
    for (auto str : strings) {
        result += str;
    }
    return result;
}

int main() {
    vector<string> strings = {"a", "b", "c"};
    string concatenated = concatenate(strings);
    cout << concatenated << endl;
    return