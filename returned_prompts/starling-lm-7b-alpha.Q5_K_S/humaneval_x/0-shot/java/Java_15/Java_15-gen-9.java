        if(n == 0)
            return "0";
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i <= n; i++) {
            sb.append(i);
            sb.append(" ");
        }
        return sb.toString().trim();
    }

    /**
    Return a string containing space-delimited numbers starting from 0 upto n-1 exclusive.
    >>> exclusiveSequence(0)
    ""
    >>> exclusiveSequence(5)
    "0 1 2 3 4"
     */
    public String exclusiveSequence(int n) {
        if(n == 0)
            return "";
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            sb.append(i);
            sb.append(" ");
        }
        return sb.toString().trim();
    }
}

class Test
{
    public static void main(String []args)
    {
        Solution solution = new Solution();
        System.out.println(solution.stringSequence(0));
        System.out.println(solution.stringSequence(5));
        System.out.println(solution.exclusiveSequence(0));
        System.out.println(solution.exclusiveSequence(5));
    }
}








































































































































































































