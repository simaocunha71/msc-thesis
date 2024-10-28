        List<String> result = new ArrayList<>();
        StringBuilder current = new StringBuilder();

        for (char c : string.toCharArray()) {
            current.append(c);
            result.add(current.toString());
        }
        return result;
    }
}

