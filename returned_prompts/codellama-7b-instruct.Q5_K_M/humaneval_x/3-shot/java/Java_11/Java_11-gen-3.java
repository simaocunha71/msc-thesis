        StringBuilder result = new StringBuilder();
        int carry = 0;

        for (int i = 0; i < Math.min(a.length(), b.length()); i++) {
            int sum = carry + Integer.parseInt(a.charAt(i) + "") ^ Integer.parseInt(b.charAt(i) + "");
            result.append(sum % 2);
            carry = sum / 2;
        }

        for (int i = Math.max(a.length(), b.length()); i > 0; i--) {
            int sum = carry + Integer.parseInt(a.charAt(i - 1) + "") ^ Integer.parseInt(b.charAt(i - 1) + "");
            result.insert(0, sum % 2);
            carry = sum / 2;
        }

        return result.toString();
    }
}

