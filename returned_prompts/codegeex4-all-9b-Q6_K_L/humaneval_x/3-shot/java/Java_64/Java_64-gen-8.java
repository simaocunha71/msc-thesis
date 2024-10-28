        int count = 0;
        String vowels = "aeiouAEIOU";
        for (int i = 0; i < s.length(); i++) {
            if (vowels.contains(String.valueOf(s.charAt(i)))) {
                count++;
            }
        }
        if (s.endsWith("y") || s.endsWith("Y")) {
            count++;
        }
        return count;
    }
}

