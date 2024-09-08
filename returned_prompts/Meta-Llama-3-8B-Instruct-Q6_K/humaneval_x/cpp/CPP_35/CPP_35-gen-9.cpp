    float max = l[0];
    for (int i = 1; i < l.size(); i++) {
        if (l[i] > max) {
            max = l[i];
        }
    }
    return max;

}

int main() {
    vector<float> v = {1, 2, 3};
    printf("%f", max_element(v));
    return 0;
}
