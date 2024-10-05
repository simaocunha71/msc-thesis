    int max_freq = -1;
    int max_num = -1;
    for (int num : lst) {
        if (num > max_num && count(lst.begin(), lst.end(), num) >= num) {
            max_freq = num;
            max_num = num;
        }
    }
    return max_freq == -1 ? -1 : max_num;
}
// Function to find the frequency of an element
int count(vector<int>::iterator start, vector<int>::iterator end, int num) {
    int count = 0;
    for (; start != end; start++) {
        if (*start == num)
            count++;
    }
    return count;
}  // Function to find the frequency of an element


