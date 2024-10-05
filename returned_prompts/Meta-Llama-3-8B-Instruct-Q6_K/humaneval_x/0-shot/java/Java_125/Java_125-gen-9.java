    public Object splitWords(String txt) {
        List<String> result = new ArrayList<>();
        StringBuilder temp = new StringBuilder();
        for (char c : txt.toCharArray()) {
            if (Character.isWhitespace(c)) {
                if (temp.length() > 0) {
                    result.add(temp.toString());
                    temp.setLength(0);
                }
            } else if (c == ',') {
                if (temp.length() > 0) {
                    result.add(temp.toString());
                    temp.setLength(0);
                }
                if (temp.length() == 0) {
                    result.add(String.valueOf(c));
                }
            } else {
                temp.append(c);
            }
        }
        if (temp.length() > 0) {
            result.add(temp.toString());
        }
        if (result.size() == 0) {
            int count = 0;
            for (char c : txt.toLowerCase().toCharArray()) {
                if (c >= 'a' && c <= 'z' && (c - 'a') % 2 == 1) {
                    count++;
                }
            }
            return count;
        }
        return result;
    }    }

The solution is designed to handle the given requirements. It iterates through each character in the string, checking if it's a whitespace or a comma. If it's a whitespace or a comma, it adds the current temporary string to the result list and resets the temporary string. If it's a non-whitespace character, it appends it to the temporary string.

If the input string contains no whitespaces or commas, it counts the number of lowercase letters with odd order in the alphabet and returns the count. It converts the string to lowercase and iterates through each character, checking if it's a lowercase letter between 'a' and 'z' and if its ASCII value minus the ASCII value of 'a' is odd. If both conditions are met, it increments the count.

The function returns either the list of split words or the count of lowercase letters with odd order in the alphabet, depending on the input string.    }    }    }    }    }    }    }    }    }    }    }    }    }    }    }    }    }    }    }    }    }    }    }    }    }    }    }    }    }    }    }    }    }    }    }    }    }    }    }    }    }    }    }    }