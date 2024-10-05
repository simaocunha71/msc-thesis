        List<String> result = new ArrayList<>();
        result.add(String.valueOf(string.charAt(0)));
        for (int i = 1; i < string.length(); i++) {
            result.add(result.get(result.size() - 1) + String.valueOf(string.charAt(i)));
        }
        result.add(string);
        return result;
    }
}

