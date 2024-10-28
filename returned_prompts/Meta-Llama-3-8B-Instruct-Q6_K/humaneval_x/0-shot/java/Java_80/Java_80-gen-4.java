        if (s.length() < 3) return false; // if the length of the string is less than 3, it is not happy
        for (int i = 0; i < s.length() - 2; i++) {
            if (s.substring(i, i + 3).chars().distinct().count() < 3) return false; // check if every 3 consecutive letters are distinct
        }
        return true; // if no distinct letters found, it is a happy string
    }
}
