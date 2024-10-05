        String result = string;
        int i = 0;
        int j = string.length() - 1;
        while (i < j) {
            if (string.charAt(i) != string.charAt(j)) {
                String left = string.substring(0, i);
                String right = string.substring(i, j + 1);
                String left_reverse = new StringBuilder(left).reverse().toString();
                String new_right = right.substring(right.length() - 1);
                result = left + new_right + left_reverse;
                return result;
            }
            i++;
            j--;
        }
        return result;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.makePalindrome("cata"));
    }
}

