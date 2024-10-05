    return sorted(arr, reverse=True)[:k] if k <= len(arr) else []  # Add error handling for k > len(arr) if needed


