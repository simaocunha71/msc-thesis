        String b2 = b + b;

        for (int i = 0; i < b.length(); i++) {
            if (b2.contains(a)) {
                return true;
            }
            b = b.substring(1) + b.charAt(0);
        }
        return false;
    }
}

