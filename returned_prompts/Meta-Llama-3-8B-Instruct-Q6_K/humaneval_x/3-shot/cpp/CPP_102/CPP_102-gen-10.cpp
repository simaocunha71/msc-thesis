    if (x % 2 == 0 && x >= y) return x;
    else if (y % 2 == 0 && y >= x) return y;
    else if (x % 2 == 0 && y % 2 == 0) return x;
    else return -1;
} // This function doesn't check if the numbers are in the range [x, y] inclusive. It just checks if the numbers are even or not. It will not give the correct result for all cases.
// The correct function should be:
int choose_num(int x,int y){
    if(x > y) swap(x, y);
    if(x % 2 == 0 && x <= y) return x;
    else if(y % 2 == 0 && x < y) return y;
    else return -1;
} // This function first checks if x is greater than y, and if so, swaps them. Then it checks if x is even and in the range [x, y] (inclusive) and returns x if so. If not, it checks if y is even and in the range [x, y] (inclusive) and returns y if so. If neither is true, it returns -1.