        List<String> result = new ArrayList<>();
        for (int length = 0; length <= string.length(); length++) {
            result.add(string.substring(0, length));
        }
        return result;
    }
}

