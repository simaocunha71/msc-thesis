
You are missing #include <algorithm> in your first and second program which includes the abs() function.
Your second program has an issue when the level is negative. You should return false immediately when the level is negative.
Your third program can be simplified. You can return true when the number is 0 and false when the number is not.
Your fourth program has a minor issue. The return true statement should be outside of the loop.