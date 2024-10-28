        for (int i = 0; i < a.length(); i++) {
            String temp = a.substring(i) + a.substring(0, i);
            if (temp.contains(b)) {
                return true;
            }
        }
        return false;
    }
}

