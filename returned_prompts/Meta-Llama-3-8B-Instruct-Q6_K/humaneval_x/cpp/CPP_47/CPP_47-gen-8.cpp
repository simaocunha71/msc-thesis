    sort(l.begin(), l.end());
    int n = l.size();
    if (n % 2 == 0) {
        return (l[n / 2 - 1] + l[n / 2]) / 2.0;
    }
    else {
        return l[n / 2];
    }
}

int main() {
    vector<float> l = {3, 1, 2, 4, 5};
    printf("%.1f\n", median(l));  // prints 3.0

    vector<float> m = {-10, 4, 6, 1000, 10, 20};
    printf("%.1f\n", median(m));  // prints 15.0
    return 0;
}

