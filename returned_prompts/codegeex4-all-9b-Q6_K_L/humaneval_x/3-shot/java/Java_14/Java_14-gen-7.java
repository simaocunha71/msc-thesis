        List<String> result = new ArrayList<>();
        StringBuilder current_string = new StringBuilder();

        for (char c : string.toCharArray()) {
            current_string.append(c);
            result.add(current_string.toString());
        }
        return result;
    }
}

