        char[] charArray = s.toCharArray();
        Arrays.sort(charArray);
        StringBuilder result = new StringBuilder();
        for (char c : charArray) {
            result.append(c);
        }
        return result.toString();
    }
}

