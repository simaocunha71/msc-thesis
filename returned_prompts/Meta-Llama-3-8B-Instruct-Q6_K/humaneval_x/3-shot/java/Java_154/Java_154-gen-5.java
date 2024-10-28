        for (int i = 0; i < b.length(); i++) {
            String s = b.substring(i) + b.substring(0, i);
            if (a.contains(s)) return true;
        }
        return false;
    }
}

