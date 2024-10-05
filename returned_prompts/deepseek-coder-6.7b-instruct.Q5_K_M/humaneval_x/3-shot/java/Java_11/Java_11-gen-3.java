        StringBuilder result = new StringBuilder();

        for(int i = 0; i < a.length(); i++){
            result.append(charXor(a.charAt(i), b.charAt(i)));
        }

        return result.toString();
    }

    private char charXor(char a, char b){
        return (char)(((a - '0') ^ (b - '0')) + '0');
    }
}

