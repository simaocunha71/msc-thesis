    int pos = s.find("apples");
    int pos2 = s.find("oranges");
    int pos3 = s.find("and");

    int apples = stoi(s.substr(0, pos));
    int oranges = stoi(s.substr(pos3 + 1, pos2 - pos3 - 1));

B:
    int mangoes = n - apples - oranges;

C:
    return mangoes;
}

int main() {
    string s = "5 apples and 6 oranges";
    int n = 19;
    printf("%d", fruit_distribution(s, n));
    return 0;
}

