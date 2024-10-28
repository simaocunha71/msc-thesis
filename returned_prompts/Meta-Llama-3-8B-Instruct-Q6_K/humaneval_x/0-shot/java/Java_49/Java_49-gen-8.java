public class Solution {
    public int modp(int n, int p) {
        if (n == 0) {
            return 1;
        }
        int res = modp(n / 2, p);
        if ((n & 1) == 1) {
            res = (res * res) % p;
        }
        return res;
    }
}
