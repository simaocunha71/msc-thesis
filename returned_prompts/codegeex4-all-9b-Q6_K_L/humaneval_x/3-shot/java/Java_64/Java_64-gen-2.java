        String vowels = "aeiou";
        int count = 0;
        for (char c : s.toCharArray()) {
            if (vowels.contains(c + "")) {
                count += 1;
            }
        }
        return count;
    }
}

