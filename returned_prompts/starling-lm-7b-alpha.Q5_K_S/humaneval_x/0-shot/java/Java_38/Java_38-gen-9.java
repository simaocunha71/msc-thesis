        List<String> groups = new ArrayList<>();
        for (int i = 0; i < s.length(); i += 3) {
            String sub = s.substring(i, Math.min(i + 3, s.length()));
            if (sub.length() == 3) {
                groups.add(sub);
                continue A;
            }
            if (sub.length() == 2) {
                String last = groups.remove(groups.size() - 1);
                groups.add(last + sub);
                continue A;
            }
            if (sub.length() == 1) {
                String last = groups.remove(groups.size() - 1);
                String before = groups.remove(groups.size() - 1);
                groups.add(before.substring(1) + before.charAt(0) + last + sub);
                continue A;
            }
        }
        return String.join("", groups);
    }

}


// Cyclic Encoding and Decoding

// Given a string, encode it by cycling the groups of three characters.
// For example, if the input is "abcde", the output would be "cdeaba".

// Decode the encoded string back to its original form.


// Solution:
// Cyclic Encoding:
// The idea of cyclic encoding is to split the string to groups, each of length 3, and then cycle the elements within each group, unless the group has less than 3 elements.
// Cyclic Decoding:
// To decode the cyclic encoding, we do the reverse process. We iterate through the string, and if the current substring has a length of 3, we add it to the result. If it has a length of 2, we add the previous group to the result, and then add the current group. If the current substring has a length of 1, we add the previous two groups to the result, and then add the current substring.















































