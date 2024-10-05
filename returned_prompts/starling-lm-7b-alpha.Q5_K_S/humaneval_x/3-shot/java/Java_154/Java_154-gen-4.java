        for (int i = 0; i < a.length(); i++) {
            if (a.contains(b)) return true;
            if (i + b.length() > a.length()) continue;
            String sub = a.substring(i, i + b.length());
            if (sub.equals(b)) return true;
            char[] ca = a.toCharArray();
            char[] cb = b.toCharArray();
            for (int j = 0; j < cb.length; j++) {
                ca[i + j] = cb[cb.length - j - 1];
            }
            sub = new String(ca);
            if (sub.equals(b)) return true;
        }
        return false;
    }
}

