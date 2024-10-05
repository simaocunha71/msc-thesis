        boolean result = false;
        for (int i = 0; i < a.length(); i++) {
            for (int j = 0; j < b.length(); j++) {
                if (a.indexOf(b.charAt(j) + "" + b.charAt((j + 1) % b.length())) > -1) {
                    result = true;
                    break;
                }
            }
        }
        return result;
    }
}



public class CodeChallenge {

    public static void main(String[] args) {
        Solution solution = new Solution();
    }
}

```