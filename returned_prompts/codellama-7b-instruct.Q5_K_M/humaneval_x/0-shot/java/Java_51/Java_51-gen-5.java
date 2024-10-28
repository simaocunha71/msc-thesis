        for (int i=0; i<text.length(); i++) {
            if (text.charAt(i)=='a' || text.charAt(i)=='e' || text.charAt(i)=='i' || text.charAt(i)=='o' || text.charAt(i)=='u' || text.charAt(i)=='A' || text.charAt(i)=='E' || text.charAt(i)=='I' || text.charAt(i)=='O' || text.charAt(i)=='U') {
                text = text.substring(0, i) + text.substring(i+1);
                i--;
            }
        }
        return text;
    }
}















