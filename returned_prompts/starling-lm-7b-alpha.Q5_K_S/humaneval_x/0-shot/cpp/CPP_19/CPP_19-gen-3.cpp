    map<string,int> mp;
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

    string res = "";
    for(int i = 0; i < numbers.length(); i++) {
        if(numbers[i] == ' ') {
            char c = numbers[i - 1];
            int index = mp[string(&c, 1)];
            for(int j = 0; j < res.length(); j++) {
                if(index < mp[string(&res[j], 1)]) {
                    char tmp = res[j];
                    res[j] = c;
                    c = tmp;
                }
            }
            res += c;
        }
    }
    return res;
}

int main() {
    printf("%s\n",sort_numbers("three one five").c_str());
    printf("%s\n",sort_numbers("three five one").c_str());
    printf("%s\n",sort_numbers("three zero").c_str());
    printf("%s\n",sort_numbers("three zero one").c_str());
    printf("%s\n",sort_numbers("three one five").c_str());
    printf("%s\n",sort_numbers("three one five five").c_str());
    printf("%s\n",sort_numbers("three zero one five").c_str());
    printf("%s\n",sort_numbers("three zero one five five").c_str());
    printf("%s\n",sort_numbers("three zero one five five zero").c_str());
    printf("%s\n",sort_numbers("three zero one five five zero one").c_str());
    printf("%s\n",sort_numbers("zero one five five zero