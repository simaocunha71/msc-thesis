    return true;
}
int main()
{
    vector<float> l1 = {1, 2, 4, 20};
    vector<float> l2 = {1, 20, 4, 10};
    vector<float> l3 = {4, 1, 0, -10};
    vector<float> l4 = {1, 2, 4, 10, 10000};

    bool b1 = monotonic(l1);
    bool b2 = monotonic(l2);
    bool b3 = monotonic(l3);
    bool b4 = monotonic(l4);
    printf("%d\n", b1);
    printf("%d\n", b2);
    printf("%d\n", b3);
    printf("%d\n", b4);
}

