        for (int i = 0; i < a.length(); i++) {
            StringBuffer s = new StringBuffer(a);
            for (int j = 0; j < b.length(); j++) {
                s.deleteCharAt(0);
                s.append(b.charAt(j));
                if (a.contains(s.toString())) {
                    return true;
                }
            }
        }

        return false;
    }
}
