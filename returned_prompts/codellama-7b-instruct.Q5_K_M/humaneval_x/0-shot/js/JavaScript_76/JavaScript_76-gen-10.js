const isSimplePower = (x, n) => {
    if(x < 2 || n < 2) return false;
    let pow = n;
    while(pow < x) {
        pow *= n;
    }
    return pow === x;
};
