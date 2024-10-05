    int d, m, y, l;
    d = date[3] - '0';
    d += (date[4] - '0') * 10;
    m = date[0] - '0';
    m += (date[1] - '0') * 10;
    y = date[6] - '0';
    y += (date[7] - '0') * 10;
    y += (date[8] - '0') * 100;
    y += (date[9] - '0') * 1000;
    if (date.size() != 10)
        return false;
    if (date[2] != '-')
        return false;
    if (date[5] != '-')
        return false;
    if (m < 1 || m > 12)
        return false;
    if (d < 1 || d > 31) {
        if (m == 1 || m == 3 || m == 5 || m == 7 || m == 8 || m == 10 || m == 12) {
            return false;
        }
    }
    if (d < 1 || d > 30) {
        if (m == 4 || m == 6 || m == 9 || m == 11) {
            return false;
        }
    }
    if (m == 2) {
        if (d < 1 || d > 29) {
            return false;
        }
    }
    if (y < 1 || y > 9999)
        return false;
    return true;
}

int main()
{
    string s;
    cin >> s;
    if (valid_date(s))
        printf("true\n");
    else
        printf("false\n");
}

































































