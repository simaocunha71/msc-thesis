return all_of(l.begin(), l.end(), [t](int x) { return x < t; });
}
