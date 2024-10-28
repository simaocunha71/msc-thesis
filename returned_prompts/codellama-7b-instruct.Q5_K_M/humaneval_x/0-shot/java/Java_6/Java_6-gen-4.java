            // Initialize counters for the max depth
            int max_depth = 0;
            int depth_counter = 0;
            // B:
            // Iterate through the characters in the string
            for (char c : paren_group_str.toCharArray()) {
                // B1:
                if (c == '(') {
                    // B11:
                    // Increment depth counter
                    depth_counter++;
                }
                // B2:
                else if (c == ')') {
                    // B21:
                    // Decrement depth counter
                    depth_counter--;
                    // B22:
                    // If depth counter is greater than max depth, update max depth
                    if (depth_counter > max_depth) {
                        max_depth = depth_counter;
                    }
                }
            }
            // C:
            // Add the max depth to the list
            depth_list.add(max_depth);
        }
        // D:
        return depth_list;
    }
}
