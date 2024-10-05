        s = s.toLowerCase();
        String vowels = "aeiou";
        int result = 0;
        for (char c : s.toCharArray()) {
            if (vowels.indexOf(c) != -1) result += 1;
        }
        return result;
    }
}

