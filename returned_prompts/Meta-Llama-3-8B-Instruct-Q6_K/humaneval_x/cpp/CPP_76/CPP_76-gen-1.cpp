    double root = pow(n, 1.0 / log(x) / log(n));
    if (fmod(root, 1) != 0) {
        return false;
    }
    return true;
}
int main() {
    printf("%d\n", is_simple_power(8, 2));
    return 0;
}