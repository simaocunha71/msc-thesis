    int sum1 = 0, sum2 = 0;
    for(auto s: lst1) sum1 += s.size();
    for(auto s: lst2) sum2 += s.size();
    return sum1 < sum2 ? lst1 : lst2;
}


int main() {
    vector<string> v1 = {"hi", "admin"};
    vector<string> v2 = {"hI", "Hi"};
    vector<string> res = total_match(v1,v2);
    for(auto s: res) printf("%s\n", s.c_str());
    return 0;
}

This program calculates the total number of chars in the strings of the vectors, compares them, and returns the vector with a lower total number of chars. If both totals are equal, it returns the first vector.
*/

int main() {
    vector<string> v1 = {"hi", "admin"};
    vector<string> v2 = {"hI", "Hi"};
    vector<string> res = total_match(v1,v2);
    for(auto s: res) printf("%s\n", s.c_str());
    return 0;
}

This program calculates the total number of chars in the strings of the vectors, compares them, and returns the vector with a lower total number of chars. If both totals are equal, it returns the first vector.
*/

int main() {
    vector<string> v1 = {"hi", "admin"};
    vector<string> v2 = {"hI", "Hi"};
    vector<string> res = total_match(v1,v2);
    for(auto s: res) printf("%s\n", s.c_str());
    return 0;
}

This program calculates the total number of chars in the strings of the vectors, compares them, and returns the vector with a lower total number of chars. If both totals are equal, it returns the first vector.
*/

int main() {
    vector<string> v1 = {"hi", "admin"};
    vector<string> v2 = {"h