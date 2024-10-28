/*
#include <cctype>

bool valid_digit_count(const std::string &file_name) {
    int digit_count = 0;
    for(char c : file_name) {
        if(std::isdigit(c)) {
            digit_count++;
        }
    }
    return digit_count <= 3;
}

bool valid_dot_count(const std::string &file_name) {
    int dot_count = 0;
    for(char c : file_name) {
        if(c == '.') {
            dot_count++;
        }
    }
    return dot_count == 1;
}

bool valid_start_char(const std::string &file_name) {
    return std::isalpha(file_name[0]);
}

bool valid_extension(const std::string &file_name) {
    std::string extension = file_name.substr(file_name.find_last_of('.') + 1);
    return extension ==