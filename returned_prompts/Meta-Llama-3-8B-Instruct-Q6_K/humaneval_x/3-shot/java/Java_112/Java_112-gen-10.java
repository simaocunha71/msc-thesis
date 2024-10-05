        List<Object> result = new ArrayList<>();
        String temp = "";
        for (int i = 0; i < s.length(); i++) {
            boolean flag = false;
            for (int j = 0; j < c.length(); j++) {
                if (s.charAt(i) == c.charAt(j)) {
                    flag = true;
                    break;
                }
            }
            if (!flag) {
                temp += s.charAt(i);
            }
        }
        result.add(temp);
        result.add(isPalindrome(temp));
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

