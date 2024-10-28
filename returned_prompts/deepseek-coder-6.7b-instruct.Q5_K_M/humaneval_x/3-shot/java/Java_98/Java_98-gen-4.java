        int count = 0;
        String upperCaseVowels = "AEIOU";

        for (int i = 0; i < s.length(); i += 2) {
            if (upperCaseVowels.indexOf(s.charAt(i)) != -1) {
                count++;
            }
        }

        return count;
    }
}

