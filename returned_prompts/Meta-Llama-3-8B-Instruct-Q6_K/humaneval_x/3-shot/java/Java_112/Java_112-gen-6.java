        String new_str = "";
        for (int i = 0; i < s.length(); i++) {
            boolean found = false;
            for (int j = 0; j < c.length(); j++) {
                if (s.charAt(i) == c.charAt(j)) {
                    found = true;
                    break;
                }
            }
            if (!found) {
                new_str += s.charAt(i);
            }
        }
        List<Object> result = new ArrayList<>();
        result.add(new_str);
        result.add(isPalindrome(new_str));
        return result;
    }

    public boolean isPalindrome(String str) {
        int i = 0, j = str.length() - 1;
        while (i < j) {
            if (str.charAt(i) != str.charAt(j))
                return false;
            i++;
            j--;
        }
        return true;
    }
}