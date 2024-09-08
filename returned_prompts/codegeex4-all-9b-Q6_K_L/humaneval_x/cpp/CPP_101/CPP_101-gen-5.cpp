#include <algorithm>
#include <iterator>
#include <sstream>
#include <vector>
#include <string>

std::vector<std::string> words_string(std::string s)
{
    std::istringstream iss(s);
    std::vector<std::string> tokens{std::istream_iterator<std::string>{iss},
 std::istream_iterator<std::string>{}};
    return tokens;
}

B:
#include <sstream>
#include <string>
#include <vector>

std::vector<std::string> words_string(std::string s)
{
    std::istringstream iss(s);
    std::vector<std::string> tokens;
    std::string token;
    while (std::getline(iss, token, ','))
    {
        tokens.push_back(token);
    }

    return tokens;
}

C:
#include <sstream>
#include <string>
#include <vector>

std::vector<std::string> words_string(std::string s)
{
    std::istringstream iss(s);
    std::vector<std::string> tokens;
    std::string token;
    while (std::getline(iss, token, ' '))
    {
        tokens.push_back(token);
    }

    return tokens;
}

D:
#include <sstream>
#include <string>
#include <vector>

std::vector<std::string> words_string(std::string s)
{
    std::istringstream iss(s);
    std::vector<std::string> tokens;
    std::string token;
    while (std::getline(iss, token, ' '))
    {
        tokens.push_back(token);
    }
    return tokens;
}

E:
#include <sstream>
#include <string>
#include <vector>

std::vector<std::string> words_string(std::string s)
{
    std::istringstream iss(s);
    std::vector<std::string> tokens;
    std::string token;
    while (std::getline(iss, token, ' '))
    {
        tokens.push_back(token);
    }
    tokens.push_back("\n");
    return tokens;
}

F:
#include <sstream>
#include <string>
#include <vector>

std::vector<std::string> words_string(std::string s)
{
    std::istringstream iss(s);
    std::vector<std::string> tokens;
    std::string token;
    while (std::getline(iss, token, ' '))
    {
        tokens.push_back(token);
    }
    tokens.push_back("\n");
    tokens.push_back("\t");
    return tokens;
}

G:
#include <sstream>
#include <string>
#include <vector