The code seems correct. It should work fine. Here is a small test:

#include <iostream>
int main() {
    std::vector<std::string> vec = words_string("Hi, my name is John");
    for(std::string str : vec) {
        std::cout << str << std::endl;
    }
    return 0;
}

This should print:
Hi
my
name
is
John

On each line.

Please, let me know if you need any other help.

A: The code seems correct. It should work fine. Here is a small test:

#include <iostream>
int main() {
    std::vector<std::string> vec = words_string("Hi, my name is John");
    for(std::string str : vec) {
        std::cout << str << std::endl;
    }
    return 0;
}

This should print:
Hi
my
name
is
John

On each line.

Please, let me know if you need any other help.

A: The code seems correct. It should work fine. Here is a small test:

#include <iostream>
int main() {
    std::vector<std::string> vec = words_string("Hi, my name is John");
    for(std::string str : vec) {
        std::cout << str << std::endl;
    }
    return 0;
}

This should print:
Hi
my
name
is
John

On each line