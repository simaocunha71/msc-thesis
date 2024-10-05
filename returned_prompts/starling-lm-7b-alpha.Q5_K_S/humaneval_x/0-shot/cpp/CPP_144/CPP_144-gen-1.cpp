    int a = x[0] - '0';
    int b = n[0] - '0';
    int c = x[2] - '0';
    int d = n[2] - '0';
    int e = x[4] - '0';
    int f = n[4] - '0';
    int g = d;
    int h = f;
    while (g != 0 && h != 0)
    {
        if (g > h)
            g = g % h;
        else
            h = h % g;
    }
    if (g == 0)
    {
        if (c * d == e * b)
        {
            if ((c * d) % b == 0)
            {
                return true;
            }
            else
            {
                return false;
            }
        }
        else
        {
            return false;
        }
    }
    else
    {
        return false;
    }
}













































































































































































































































































