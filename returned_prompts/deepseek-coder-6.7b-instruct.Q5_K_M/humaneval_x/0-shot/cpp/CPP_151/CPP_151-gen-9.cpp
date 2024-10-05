    long long sum = 0;
    for (int i = 0; i < lst.size(); i++) {
        if (lst[i] > 0 && lst[i] == floor(lst[i]) && (int)lst[i] % 2 != 0) {
            sum += pow((int)lst[i], 2);
        }
    }
    return sum;
}

int main() {
    vector<float> lst = {1, 3, 2, 0};
    printf("%lld", double_the_difference(lst));
    return 0;
}

Output:
10
*/

int main() {
    vector<float> lst = {1, 3, 2, 0};
    printf("%lld", double_the_difference(lst));
    return 0;
}
/*
OUTPUT:
10
*/

int main() {
    vector<float> lst = {-1, -2, 0};
    printf("%lld", double_the_difference(lst));
    return 0;
}
/*
OUTPUT:
0
*/

int main() {
    vector<float> lst = {9, -2};
    printf("%lld", double_the_difference(lst));
    return 0;
}
/*
OUTPUT:
81
*/

int main() {
    vector<float> lst = {0};
    printf("%lld", double_the_difference(lst));
    return 0;
}
/*
OUTPUT:
0
*/

int main() {
    vector<float> lst = {};
    printf("%lld", double_the_difference(lst));
    return 0;
}
/*
OUTPUT:
0
*/




































































