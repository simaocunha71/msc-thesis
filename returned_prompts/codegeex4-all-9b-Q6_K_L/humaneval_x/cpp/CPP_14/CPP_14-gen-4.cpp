#include <vector>
#include <string>

std::vector<std::string> all_prefixes(std::string str) {
    std::vector<std::string> prefixes;

    for (int i = 0; i < str.size(); i++) {
        prefixes.push_back(str.substr(0, i + 1));
    }

    return prefixes;
}

