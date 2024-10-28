        int i = string.length() - 1;
        int j = string.length() - 1;
        while (i >= 0) {
            if (isPalindrome(string.substring(i, j + 1))) {
                break;
            }
            i--;
            j--;
        }
        if (i < 0) {
            return string;
        }
        StringBuffer sb = new StringBuffer(string.substring(0, i + 1));
        sb.append(string.substring(j, string.length()));
        sb.reverse();
        return sb.toString();
    }
    public static void main(String[] args) {
        Solution sl = new Solution();
        String s = "catac";
        System.out.println(sl.makePalindrome(s));
    }
}
