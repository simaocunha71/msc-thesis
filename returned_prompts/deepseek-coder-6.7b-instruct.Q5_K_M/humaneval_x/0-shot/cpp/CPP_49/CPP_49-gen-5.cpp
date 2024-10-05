    int i, j, k, l, m, o, q[100], r[100], s[100], t[100], u[100];
    i = 0;
    j = 0;
    k = 0;
    l = 0;
    m = 0;
    o = 0;
    q[0] = 1;
    r[0] = 2;
    s[0] = 1;
    t[0] = 0;
    u[0] = 0;
    while (i <= n){
        while ((j <= i) && (j < p)){
            m = j;
            while (m >= 0){
                if ((q[m] - r[m] * q[j - m] % p) < 0){
                    q[m] = q[m] - r[m] * q[j - m] % p + p;
                }
                else {
                    q[m] = q[m] - r[m] * q[j - m] % p;
                }
                m = m - 1;
            }
            if (j < p - 1){
                r[j + 1] = r[j] * r[0] % p;
            }
            j = j + 1;
        }
        while ((k <= i) && (k < p)){
            o = k;
            while (o >= 0){
                if ((s[o] - r[o] * s[k - o] % p) < 0){
                    s[o] = s[o] - r[o] * s[k - o] % p + p;
                }
                else {
                    s[o] = s[o] - r[o] * s[k - o] % p;
                }
                o = o - 1;
            }
            if (k < p - 1){
                r[k + 1] = r[k] * r[0] % p;
            }
            k = k + 1;
        }
        while ((l <= i) && (l < p)){
            o = l;
            while (o >= 0