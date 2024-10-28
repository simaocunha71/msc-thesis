        boolean lowerCase = true, upperCase = true;

        for (Object key : dict.keySet()) {
            if (!(key instanceof String)) return false;
            if (((String) key).toLowerCase().equals(key)) lowerCase = false;
            if (((String) key).toUpperCase().equals(key)) upperCase = false;
        }
        return !(lowerCase && upperCase);
    }
}

