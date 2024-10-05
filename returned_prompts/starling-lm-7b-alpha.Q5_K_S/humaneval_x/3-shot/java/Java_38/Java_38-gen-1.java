        StringBuilder result = new StringBuilder();
        for (int i = 0; i < s.length(); i++) {
            result.insert(0, s.charAt(i));
            if ((i + 1) % 3 == 0) result.append(s.charAt(i));
        }
        return result.toString();
    }
}

