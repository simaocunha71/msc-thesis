    var result []int
    var current int
    for _, p := range strings.Split(paren_string, " ") {
        current = 0
        for _, c := range p {
            if c == '(' {
                current += 1
            } else if c == ')' {
                current -= 1
            }
            if current > result[len(result)-1] {
                result = append(result, current)
            }
        }
    }
    return result
}










#include <iostream>
#include <vector>
#include <string>
#include <cstdint>
#include <cctype>

std::vector<int> parse_nested_parens(const std::string& paren_string) {
    std::vector<int> result;
    int current = 0;
    for (auto p : paren_string) {
        if (p == '(') {
            ++current;
        } else if (p == ')') {
            --current;
        }
        if (current > result.back()) {
            result.push_back(current);
        }
    }
    return result;
}

int main() {
    std::cout << parse_nested_parens("(()()) ((())) () ((())()())") << std::endl;
}




# ParseNestedParens('(()()) ((())) () ((())()())')
# [2, 3, 1, 3]
def parse_nested_parens(paren_string):
    result = []
    current = 0
    for _, p in enumerate(paren_string.split(" ")):
        current = 0
        for _, c in enumerate(p):
            if c == '(':
                current += 1
            elif c == ')':
                current -= 1
            if current > result[-1]:
                result.append(current)
    return result

parseNestedParens('(()()) ((())) () ((())()())')






















