        List<String> prefixes = new ArrayList<String>();
        for(int i = 0; i < string.length(); i++) {
            prefixes.add(string.substring(0, i+1));
        }
        return prefixes;
    }
}

