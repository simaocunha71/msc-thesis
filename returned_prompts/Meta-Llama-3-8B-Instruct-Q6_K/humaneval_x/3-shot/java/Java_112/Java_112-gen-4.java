        List<Object> result = new ArrayList<>();
        StringBuilder temp = new StringBuilder();
        for (char c1 : s.toCharArray()) {
            if (!c.contains(String.valueOf(c1))) {
                temp.append(c1);
            }
        }
        result.add(temp.toString());
        result.add(isPalindrome(temp.toString()));
        return result;
    }

    public boolean isPalindrome(String s) {
        int i = 0, j = s.length() - 1;
        while (i < j) {
            if (s.charAt(i) != s.charAt(j)) {
                return false;
            }
            i++;
            j--;
        }
        return true;
    }
}