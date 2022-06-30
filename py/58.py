def length_of_lastWord(string: str) -> int:
    return len(string.rstrip().split(" ")[-1])


print(length_of_lastWord("   fly me   to   the moon  "))
