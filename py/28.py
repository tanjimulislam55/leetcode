def str_str(haystack: str, needle: str) -> int:
    if needle not in haystack:
        return -1
    return len(haystack.split(needle)[0])
