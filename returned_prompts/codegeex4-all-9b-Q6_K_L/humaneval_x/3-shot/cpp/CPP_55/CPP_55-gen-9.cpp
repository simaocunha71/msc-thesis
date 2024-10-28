
Your functions are correct, and they are well-commented. I like that.
Code Organization
You've included all the necessary headers, and it appears you are using C++11 (since you are using auto). If that's the case, you can drop the using namespace std; line. This is a good practice as it prevents name clashes, and it shows which namespace you are using.
Also, your code doesn't have any error handling. If you are going to use vectors, you should consider what happens if they are empty.
Also, you could use the more modern for loop syntax instead of the old C-style for loop.
has_close_elements
I would rather use the standard library algorithms instead of loops, but you can do it either way.
#include <algorithm>
#include <vector>
#include <cmath>

using namespace std;

bool has_close_elements(const vector<float>& numbers, float threshold) {
    auto is_close = [threshold](float a, float b) { return abs(a - b) < threshold; };

    return adjacent_find(numbers.begin(), numbers.end(), is_close) != numbers.end();
}

separate_paren_groups
This is a good problem for the standard library.
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

vector<string> separate_paren_groups(const string& paren_string) {
    vector<string> all_parens;
    string current_paren;
    int level = 0;

    for (char chr : paren_string) {
        if (chr == '(') {
            ++level;
        }
        else if (chr == ')') {
            --level;
        }
        current_paren += chr;

        if (level == 0) {
            all_parens.push_back(current_paren);
            current_paren.clear();
        }
    }

    return all_parens;
}

truncate_number
This can be done with basic math.
#include <cmath>

using namespace std;

float truncate_number(float number) {
    return number - static_cast<int>(number);
}

fib
This can be done with recursion, or with an iterative approach. I prefer the iterative approach.
#include <stdexcept>
#include <vector>

using