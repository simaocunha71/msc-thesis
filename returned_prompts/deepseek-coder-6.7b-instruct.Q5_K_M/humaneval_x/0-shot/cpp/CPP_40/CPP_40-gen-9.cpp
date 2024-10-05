    int n = l.size();
    sort(l.begin(), l.end());

B:
    for (int i = 0; i < n - 1; i++) {
        int a = l[i];
        int start = i + 1;
        int end = n - 1;
        while (start < end) {
            int b = l[start];
            int c = l[end];
            if (a + b + c == 0) {
                return true;
            } else if (a + b + c < 0) {
                start += 1;
            } else {
                end -= 1;
            }
        }
    }
    return false;
}

int main() {
    vector<int> v1 = {1, 3, 5, 0};
    vector<int> v2 = {1, 3, -2, 1};
    vector<int> v3 = {1, 2, 3, 7};
    vector<int> v4 = {2, 4, -5, 3, 9, 7};
    vector<int> v5 = {1};

    printf("%d\n", triples_sum_to_zero(v1));  // False
    printf("%d\n", triples_sum_to_zero(v2));  // True
    printf("%d\n", triples_sum_to_zero(v3));  // False
    printf("%d\n", triples_sum_to_zero(v4));  // True
    printf("%d\n", triples_sum_to_zero(v5));  // False

    return 0;
}
// Expected output:
// 0
// 1
// 0
// 1
// 0
// End of Program.
*/

The above C++ code uses the two-pointer technique to find three numbers in a sorted array that sum to zero. The array is first sorted. Then for each number 'a' from the array, it finds two other numbers 'b' and 'c' such that 'a' + 'b' + 'c' equals zero by using two pointers, one at