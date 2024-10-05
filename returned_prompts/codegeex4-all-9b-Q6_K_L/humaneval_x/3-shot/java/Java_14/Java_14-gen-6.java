        List<String> result = new ArrayList<>();

        for (int i = 1; i <= string.length(); i++) {
            String substring = string.substring(0, i);
            result.add(substring);
        }
        return result;
    }
}

