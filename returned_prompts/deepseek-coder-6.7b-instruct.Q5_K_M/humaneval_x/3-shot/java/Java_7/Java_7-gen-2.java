        List<String> result = new ArrayList<>();

        for (String string : strings) {
            if (string.contains(substring)) {
                result.add(string);
            }
        }

        return result;
    }
}

