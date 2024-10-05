    bool increasing = true;
    bool decreasing = true;
    float prev = l[0];
    for (int i = 1; i < l.size(); i++) {
        if (l[i] > prev) {
            decreasing = false;
        }
        if (l[i] < prev) {
            increasing = false;
        }
        prev = l[i];
    }
    return increasing || decreasing;
}