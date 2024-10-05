    vector<string> result;
    size_t start = 0, end = 0;

    while (end != string::npos) {
        end = s.find_first_of(", ", start);

        // If at end of string
        if (end == string::npos) {
            result.push_back(s.substr(start));
        }
        else {
            result.push_back(s.substr(start, end - start));
            // Skip comma or space
            start = end + 1;
        }
    }
    return result;
}

int main() {
    vector<string> v = words_string("Hi, my name is John");
    for(auto &s : v)
        printf("%s\n", s.c_str());
    return 0;
}

*/

int main(int argc, char *argv[]) {
    const char *str = "Hi, my name is John";
    vector<string> words = words_string(str);
    for (size_t i = 0; i < words.size(); i++) {
        printf("%s\n", words[i].c_str());
    }
    return 0;
}

//test/test_words_string.cpp
#include <gtest/gtest.h>
#include "../src/words_string.cpp"

TEST(words_string, test1) {
    std::string s = "Hi, my name is John";
    std::vector<std::string> expected = {"Hi", "my", "name", "is", "John"};
    ASSERT_EQ(expected, words_string(s));
}

TEST(words_string, test2) {
    std::string s = "One, two, three, four, five, six";
    std::vector<std::string> expected = {"One", "two", "three", "four", "five", "six"};
    ASSERT_EQ(expected, words_string(s));
}

int main(int argc, char **argv) {
    ::testing::InitGoogleTest(&argc, argv);
