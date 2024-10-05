        String vowels = "aeiouAEIOU";

        StringBuilder result = new StringBuilder();
        for (char c : text.toCharArray()) {
            if (!vowels.contains(c + "")) result.append(c);
        }
        return result.toString();
    }
}

