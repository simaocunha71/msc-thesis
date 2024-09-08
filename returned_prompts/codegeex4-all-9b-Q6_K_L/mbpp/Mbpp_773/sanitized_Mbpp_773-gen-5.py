def occurance_substring(string, substring):
    positions = [i for i in range(len(string)) if string.startswith(substring, i)]
    if not positions:
        return None
    return (substring, positions[0], positions[-1])