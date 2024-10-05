        if(n == 0) {
            return "0";
        }
        StringBuffer sb = new StringBuffer();
        for(int i = 0; i <= n; i++) {
            sb.append(i + " ");
        }
        String ans = sb.toString();
        return ans.substring(0, ans.length() - 1);
    }

    /**
    Return a string containing numbers starting from 0 upto n inclusive.
    >>> intSequence(0)
    []
    >>> intSequence(5)
    [0, 1, 2, 3, 4, 5]
     */
    public int[] intSequence(int n) {

        if(n == 0) {
            return new int[]{};
        }
        int[] seq = new int[n + 1];
        for(int i = 0; i <= n; i++) {
            seq[i] = i;
        }
        return seq;
    }

    /**
    Return a string containing space-delimited numbers starting from m upto n inclusive.
    >>> stringSequence(0, 5)
    "0 1 2 3 4 5"
    >>> stringSequence(3, 5)
    "3 4 5"
     */
    public String stringSequence(int m, int n) {
        if(m == 0) {
            return stringSequence(n);
        }
        StringBuffer sb = new StringBuffer();
        for(int i = m; i <= n; i++) {
            sb.append(i + " ");
        }
        String ans = sb.toString();
        return ans.substring(0, ans.length() - 1);
    }

    /**
    Return a string containing numbers starting from m upto n inclusive.
    >>> intSequence(3, 5)
    [3, 4, 5]
    >>> intSequence(0, 5)
    [0, 1, 2, 3, 4, 5]
     */
    public int[] intSequence(int m, int n) {
        if(m == 0) {
            return