    if  (a + b <= c || a + c <= b || b + c <= a)
        return -1;
    float s = (a + b + c) / 2;
    float area = sqrt(s * (s - a) * (s - b) * (s - c));
    return round(area * 100) / 100;
}

