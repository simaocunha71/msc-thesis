def drop_empty(d: dict):
    return {k: v for k, v in d.items() if v is not None}