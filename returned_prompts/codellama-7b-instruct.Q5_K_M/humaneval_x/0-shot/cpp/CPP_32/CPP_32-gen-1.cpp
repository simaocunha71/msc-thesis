    int i;
    double x0=0, x1, delta;
    int n=xs.size();
    if (n % 2 == 1 or xs[0] == 0)
        return 0;
    for (i=0;i<n;i++)
    {
        if (xs[i] != 0)
            x0 = i;
    }
    if (x0 == 0)
        return 0;
    x1 = x0;
    delta = 0.01;
    while (delta > 0.000001)
    {
        x1 -= poly(xs, x1) / poly(xs, x1+1);
        delta = abs(x1 - x0);
    }
    return x1;
}

