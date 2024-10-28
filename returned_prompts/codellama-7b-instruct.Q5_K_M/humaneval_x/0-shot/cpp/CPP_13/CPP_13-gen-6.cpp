if (a == b){
    return a;
}
if (a > b){
    return greatest_common_divisor(a % b, b);
}
if (a < b){
    return greatest_common_divisor(a, b % a);
}
}

