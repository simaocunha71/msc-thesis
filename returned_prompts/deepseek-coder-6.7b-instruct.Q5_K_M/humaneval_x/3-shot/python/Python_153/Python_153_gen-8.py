    def strength(extension):
        return sum(c.isupper() for c in extension) - sum(c.islower() for c in extension)

    extensions.sort(key=strength, reverse=True)
    return f"{class_name}.{extensions[0]}"


