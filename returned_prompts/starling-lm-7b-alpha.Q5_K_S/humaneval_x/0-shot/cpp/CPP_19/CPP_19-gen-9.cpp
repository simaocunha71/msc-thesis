    map<string, int> mp;
    mp["zero"] = 0;
    mp["one"] = 1;
    mp["two"] = 2;
    mp["three"] = 3;
    mp["four"] = 4;
    mp["five"] = 5;
    mp["six"] = 6;
    mp["seven"] = 7;
    mp["eight"] = 8;
    mp["nine"] = 9;
    int pos = 0;
    int len = numbers.length();
    char *str = new char[len];
    for (int i = 0; i < len; i++) {
        if (numbers[i] == ' ') {
            str[pos++] = ',';
        }
        else {
            str[pos++] = numbers[i];
        }
    }
    str[pos] = 0;
    string ret = "";
    for (int i = 0; i < pos; i++) {
        if (str[i] == ',' || i == pos - 1) {
            if (mp[string(str + i, 1)] != 0) {
                ret += string(str + i, 1);
            }
        }
    }
    delete[] str;
    return ret;
}

int main()
{
    printf("%s", sort_numbers("three one five").c_str());
    return 0;
}







































































































































































