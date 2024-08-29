
def find_literals(s, pattern):
    match = re.search(pattern, s)
    if match:
        return (match.group(), match.start(), match.end())
    return None

print(find_literals('The quick brown fox jumps over the lazy dog.', 'fox'))
<jupyter_output>
('fox', 16, 19)
<jupyter_text>
Q2:
<jupyter_code>
