        List<String> prefixes  List<>;
        for  (int i = 0; i < string.length(); i++) {
            prefixes.add(string.substring(0, i+1));
        }
        return prefixes;
     }
}

