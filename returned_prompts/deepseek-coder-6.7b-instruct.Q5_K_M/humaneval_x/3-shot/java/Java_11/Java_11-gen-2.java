        StringBuilder result = new StringBuilder();

        for(int i = 0; i < a.length(); i++) {
            result.append(Character.getNumericValue(a.charAt(i)) ^ Character.getNumericValue(b.charAt(i)));
        }
        return result.toString();
     }
}

