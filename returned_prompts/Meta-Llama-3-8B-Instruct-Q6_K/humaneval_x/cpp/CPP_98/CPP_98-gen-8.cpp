    int count = 0;
    for(int i = 0; i < s.length(); i++)
    {
        if(i % 2 == 0 && isupper(s[i]))
        {
            count++;
        }
    }
    return count;
}

int main()
{
    string s = "aBCdEf";
    cout << "Number of uppercase vowels in even indices is: " << count_upper(s);
    return 0;
}

B:
    int count_upper(const std::string& s) {
        int count = 0;
        for (int i = 0; i < s.size(); i++) {
            if (i % 2 == 0 && std::isupper(s[i])) {
                count++;
            }
        }
        return count;
    }
    int main() {
        std::string s = "aBCdEf";
        std::cout << "Number of uppercase vowels in even indices is: " << count_upper(s) << std::endl;
        return 0;
    }
C:
    int count_upper(const std::string& s) {
        int count = 0;
        for (auto c : s) {
            if (std::isupper(c) && std::distance(&s[0], std::next(&c)) % 2 == 0) {
                count++;
            }
        }
        return count;
    }
    int main() {
        std::string s = "aBCdEf";
        std::cout << "Number of uppercase vowels in even indices is: " << count_upper(s) << std::endl;
        return 0;
    }
D:
    int count_upper(const std::string& s) {
        int count = 0;
        for (int i = 0; i < s.size(); i++) {
            if (i % 2 == 0 && s[i] == 'A' || s[i] == 'E' || s[i] == 'I' || s[i] == 'O' || s[i] == 'U') {
                count++;
            }
        }
        return count;
    }
    int main() {
        std::string s = "aBCdEf";
        std::cout << "Number of uppercase vowels in even indices is: " << count_upper(s) << std::endl;
        return 0;
    }
E:
    int count_upper(const std::string& s) {
        int count = 0;
        for