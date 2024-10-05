        for (int i = 0; i < b.length(); i++) {
            if (a.indexOf(b.substring(i)) != -1) return true;
        }
        return false;
    }
}

