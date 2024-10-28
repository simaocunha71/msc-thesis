        for (int i = 0; i < b.length(); i++) {
            String rotated_string = b.substring(i) + b.substring(0, i);
            if (a.contains(rotated_string)) return true;
        }
        return false;
    }
}

