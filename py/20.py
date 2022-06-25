def is_valid(string: str) -> bool:
    braces = {"(": ")", "{": "}", "[": "]"}
    stack = []
    for x in string:
        if x in braces:
            stack.append(braces[x])
        else:
            if x in stack:
                if x != stack[-1]:
                    return False
                stack.pop()
            else:
                return False
    return True if len(stack) == 0 else False


print(is_valid("()[]{}"))
print(is_valid("(]"))
print(is_valid("{[]}"))
print(is_valid("([)]"))
print(is_valid("[([]])"))
