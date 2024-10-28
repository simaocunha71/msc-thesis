        List<Object> result = new ArrayList<>();
        String temp = "";
        boolean is_palindrome = false;

        for (char ch : s.toCharArray()) {
            if (!c.contains(ch + "")) {
                temp += ch;
            }
        }

        for (int i = 0; i < temp.length() / 2; i++) {
            if (temp.charAt(i) != temp.charAt(temp.length() - 1 - i)) {
                is_palindrome = false;
                break;
            } else {
                is_palindrome = true;
            }
        }

        result.add(temp);
        result.add(is_palindrome);
        return result;
    }
}

