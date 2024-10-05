        int result = 0;
        Scanner scan = new Scanner(S);
        while (scan.hasNext()) {
            String sentence = scan.next();
            if (sentence.startsWith("I")) {
                result += 1;
            }
        }
        return result;
    }
}

