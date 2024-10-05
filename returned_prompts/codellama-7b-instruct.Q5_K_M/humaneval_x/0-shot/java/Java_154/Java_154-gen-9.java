        for (int i = 0; i < b.length(); i++) {
            String s = b.substring(0, i + 1);
            if (a.contains(s)) {
                return true;
            }
        }
        return false;
    }
}

