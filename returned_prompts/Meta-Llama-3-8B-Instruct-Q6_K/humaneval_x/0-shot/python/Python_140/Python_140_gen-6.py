def fix_spaces(text):
    return text.replace(" ", "_").replace("  ", "-").replace("   ", "-").replace("    ", "-")

# Test cases
print(fix_spaces("Example"))  # "Example"
print(fix_spaces("Example 1"))  # "Example_1"
print(fix_spaces(" Example 2"))  # "_Example_2"
print(fix_spaces(" Example   3"))  # "_Example-3"
print(fix_spaces("   Example   4"))  # "_-Example-4"
print(fix_spaces("   Example   5   "))  # "_-Example-5-"
print(fix_spaces("   Example   5   6   "))  # "_-Example-5-6-"
print(fix_spaces("   Example   5   6   7   "))  # "_-Example-5-6-7-"
print(fix_spaces("   Example   5   6   7   8   "))  # "_-Example-5-6-7-8-"
print(fix_spaces("   Example   5   6   7   8   9   "))  # "_-Example-5-6-7-8-9-"
print(fix_spaces("   Example   5   6   7   8   9   10"))  # "_-Example-5-6-7-8-9-10-"  # 1.6s
print(fix_spaces("   Example   5   6   7   8   9   10   11"))  # "_-Example-5-6-7-8-9-10-11-"  # 1.7s
print(fix_spaces("   Example   5   6   7   8   9   10   11   12"))  # "_-Example-5-6-7-8-9-10-11-12-"  # 1.8s
print(fix_spaces("   Example   5   6   7   8   9   10   11   12   13"))  # "_-Example-5-6-7-8-9-10-11-12-13-"  # 2.0s
print(fix_spaces