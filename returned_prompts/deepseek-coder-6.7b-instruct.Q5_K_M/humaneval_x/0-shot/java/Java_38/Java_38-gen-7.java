        // split string to groups. Each of length 3.
        List<String> groups = new ArrayList<>();
        for (int i = 0; i < s.length(); i += 3) {
            groups.add(s.subsubstring(i, Math.min(i + 3, s.length())));
        }

        // reverse cycle elements in each group. Unless group has fewer elements than 3.
        for (int i = 0; i < groups.size(); i++) {
            if (groups.get(i).length() == 3) {
                groups.set(i, groups.get(i).charAt(2) + groups.get(i).substring(0, 2));
            }
        }

        return String.join("", groups);
    }
}

I'm getting an error here:

groups.set(i, groups.get(i).charAt(2) + groups.get(i).substring(0, 2));

It says "The method substring(int, int) in the type String is not applicable for the arguments (int)".

What am I doing wrong?

A: The problem is in this line:
groups.set(i, groups.get(i).charAt(2) + groups.get(i).substring(0, 2));

You are trying to concatenate a char with a String using the + operator, which is causing the error. You should use the StringBuilder for this. Here is the corrected code:
StringBuilder sb = new StringBuilder(groups.get(i));
sb.setCharAt(0, sb.charAt(2));
sb.deleteCharAt(2);
groups.set(i, sb.toString());

Also, you are using subsubstring method which is not valid. It should be substring.
Here is the corrected version:
groups.add(s.substring(i, Math.min(i + 3, s.length())));


A: The error is because you are trying to concatenate a char and a String using the '+' operator.
Java does not support this kind of operation directly. 

You can use StringBuilder to achieve this.
Here is the corrected code:
