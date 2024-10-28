        if (s.length() < 3) {
            return false;
        }

        for (int i = 0; i < s.length() - 2; i++) {
            if (s.charAt(i) == s.charAt(i + 1) || s.charAt(i + 1) == s.charAt(i + 2) || s.charAt(i) == s.charAt(i + 2)) {
                return false;
            }
        }

        return true;

    }
}

This code checks if the string has at least 3 characters. It then checks each set of 3 consecutive characters to see if they are all distinct. If any of the sets are not distinct, it returns false. If it gets through the entire string without finding any sets of non-distinct characters, it returns true.

