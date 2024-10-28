        if (dict.size() == 0) {
            return true;
        }

        Set<Object> keys = dict.keySet();
        Iterator<Object> it = keys.iterator();
        while (it.hasNext()) {
            Object key = it.next();
            if (key instanceof String) {
                char firstChar = ((String) key).charAt(0);
                if (!Character.isUpperCase(firstChar) && !Character.isLowerCase(firstChar)) {
                    return false;
                }
            } else {
                return false;
            }
        }
        return true;
    }
}


```