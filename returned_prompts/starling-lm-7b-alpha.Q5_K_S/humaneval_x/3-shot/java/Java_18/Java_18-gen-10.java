        int result = 0;
        for (int start = 0; start < string.length(); start++) {
            int end = start + substring.length() - 1;
            if (start + substring.length() > string.length()) break;
            if (string.substring(start, end + 1).equals(substring)) result += 1;
        }
        return result;
    }
}

