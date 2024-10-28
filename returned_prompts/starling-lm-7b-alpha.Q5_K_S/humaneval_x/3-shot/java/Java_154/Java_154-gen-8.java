        String b_rotated = rotateString(b);
        String b_rotated_2 = rotateString(b_rotated);
        String b_rotated_3 = rotateString(b_rotated_2);
        String[] b_rotations = new String[]{b, b_rotated, b_rotated_2, b_rotated_3};

        for (String b_rotated_s : b_rotations) {
            if (a.contains(b_rotated_s)) return true;
        }
        return false;
    }

    String rotateString(String b) {
        return b.substring(1, b.length()) + b.charAt(0);
    }
}

