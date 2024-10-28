        if (dict.isEmpty()) return false;

        for (Object key : dict.keySet()) {
            if (!(key instanceof String)) {
                return false;
            }
            if (!((String) key).equalsIgnoreCase((String) key)) {
                continue A;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        System.out.println(new Solution().checkDictCase(new HashMap<>()));
        System.out.println(new Solution().checkDictCase(new HashMap<>()));
        System.out.println(new Solution().checkDictCase(new HashMap<>()));
        System.out.println(new Solution().checkDictCase(new HashMap<>()));
        System.out.println(new Solution().checkDictCase(new HashMap<>()));
    }
}

