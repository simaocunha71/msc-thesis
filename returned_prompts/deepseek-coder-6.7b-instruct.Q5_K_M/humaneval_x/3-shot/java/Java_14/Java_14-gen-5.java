        List<String> result = new ArrayList<>();
        String prefix = "";
        for (int i = 0; i < string.length(); i++) {
            prefix += string.charAt(i);
            result.add(prefix);
        }
        return result;
     }
}

