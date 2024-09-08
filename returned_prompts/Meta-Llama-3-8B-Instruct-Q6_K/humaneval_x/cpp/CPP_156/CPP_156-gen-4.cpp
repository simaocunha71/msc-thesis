    // Create a map for roman numerals
    map<int, string> roman = {{1000, "m"}, {900, "cm"}, {500, "d"}, {400, "cd"}, {100, "c"}, {90, "xc"}, {50, "l"}, {40, "xl"}, {10, "x"}, {9, "ix"}, {5, "v"}, {4, "iv"}, {1, "i"}};
    string result = "";
    
    // Iterate through the map
    for(auto it = roman.begin(); it != roman.end(); ++it) {
        while(number >= it->first) {
            result += it->second;
            number -= it->first;
        }
    }
    return result;
}
B:
    return result.toLowerCase();
}
int main() {
    printf("%s\n", int_to_mini_roman(19).c_str());
    printf("%s\n", int_to_mini_roman(152).c_str());
    printf("%s\n", int_to_mini_roman(426).c_str());
    return 0;
}
C:
}
} // namespace std;
}

