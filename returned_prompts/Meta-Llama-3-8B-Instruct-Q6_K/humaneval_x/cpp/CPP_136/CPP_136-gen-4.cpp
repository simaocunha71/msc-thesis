
int main() {
    vector<int> lst1 = {2, 4, 1, 3, 5, 7};
    vector<int> lst2 = {};
    vector<int> lst3 = {0};
    vector<int> lst4 = {-5, -4, -3, -2, -1};
    vector<int> lst5 = {5, 4, 3, 2, 1};

    printf("largest_smallest_integers({2, 4, 1, 3, 5, 7}) == {%d, %d}\n", largest_smallest_integers(lst1)[0], largest_smallest_integers(lst1)[1]);
    printf("largest_smallest_integers({}) == {%d, %d}\n", largest_smallest_integers(lst2)[0], largest_smallest_integers(lst2)[1]);
    printf("largest_smallest_integers({0}) == {%d, %d}\n", largest_smallest_integers(lst3)[0], largest_smallest_integers(lst3)[1]);
    printf("largest_smallest_integers({-5, -4, -3, -2, -1}) == {%d, %d}\n", largest_smallest_integers(lst4)[0], largest_smallest_integers(lst4)[1]);
    printf("largest_smallest_integers({5, 4, 3, 2, 1}) == {%d, %d}\n", largest_smallest_integers(lst5)[0], largest_smallest_integers(lst5)[1]);

    return 0;
}
