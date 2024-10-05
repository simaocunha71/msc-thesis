        if (dict.isEmpty()) return false;

        boolean allLowerCase = true;
        boolean allUpperCase = true;

        for (Object key : dict.keySet()) {
            if (!(key instanceof String)) return false;

            String strKey = (String) key;
            if (!strKey.equals(strKey.toLowerCase())) allLowerCase = false;
            if (!strKey.equals(strKey.toUpperCase())) allUpperCase = false;
        }

        return allLowerCase || allUpperCase;
    }
}

