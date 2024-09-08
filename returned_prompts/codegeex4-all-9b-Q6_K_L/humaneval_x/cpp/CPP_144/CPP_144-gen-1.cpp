bool simplify(string x, string n) {
    int numerator_x, denominator_x, numerator_n, denominator_n;

    // 分解x和n为分子和分母
    sscanf(x.c_str(), "%d/%d", &numerator_x, &denominator_x);
    sscanf(n.c_str(), "%d/%d", &numerator_n, &denominator_n);

    // 计算乘积
    int product_numerator = numerator_x * numerator_n;
    int product_denominator = denominator_x * denominator_n;

    // 检查乘积是否为整数
    return product_numerator % product_denominator == 0;
}