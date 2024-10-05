        if(dict.isEmpty())
            return false;

        boolean allLower = true;
        boolean allUpper = true;

        for (Object key : dict.keySet()) {
            if (!(key instanceof String))
                return false;

            String strKey = (String) key;
            if (!strKey.equals(strKey.toLowerCase()))
                allLower = false;
            if (!strKey.equals(strKey.toUpperCase()))
                allUpper = false;
        }

        return allLower || allUpper;
    }
}

