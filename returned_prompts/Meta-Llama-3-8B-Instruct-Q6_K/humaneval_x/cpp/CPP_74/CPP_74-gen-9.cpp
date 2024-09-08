    vector<string> result;
    int total_chars1 = 0, total_chars2 = 0;
    for (const auto& str : lst1) {
        total_chars1 += str.length();
    }
    for (const auto& str : lst2) {
        total_chars2 += str.length();
    }
    if (total_chars1 < total_chars2) {
        result = lst1;
    } else if (total_chars1 > total_chars2) {
        result = lst2;
    } else {
        result = lst1;
    }
    return result;
}
int main() {
    vector<string> lst1 = {"hi", "admin"};
    vector<string> lst2 = {"hI", "Hi"};
    vector<string> result = total_match(lst1, lst2);
    for (const auto& str : result) {
        printf("%s\n", str.c_str());
    }
    return 0;
} // ➞ {"hI", "Hi"}


In this code, we are calculating the total number of characters in each vector by iterating through each string in the vector and adding its length to the total. Then we compare the total number of characters in both vectors. If the total number of characters in the first vector is less than the second, we return the first vector. If the total number of characters in the second vector is less than the first, we return the second vector. If the total number of characters is the same, we return the first vector.