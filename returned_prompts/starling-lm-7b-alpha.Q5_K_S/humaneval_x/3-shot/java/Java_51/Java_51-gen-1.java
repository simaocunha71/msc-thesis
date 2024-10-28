        StringBuilder result = new StringBuilder();
        for (char c : text.toCharArray()) {
            if (!"aeiouAEIOU".contains(c + "")) {
                result.append(c);
            }
        }
        return result.toString();
    }
}

