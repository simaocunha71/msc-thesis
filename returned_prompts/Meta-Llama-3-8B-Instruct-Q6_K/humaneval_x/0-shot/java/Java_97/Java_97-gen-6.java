int a1 = Math.abs(a) % 10;
int b1 = Math.abs(b) % 10;
int product = a1 * b1;
if ((a < 0) ^ (b < 0)) {
    product = -product;
}
return product;
}
