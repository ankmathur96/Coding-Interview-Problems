def braces(value):
    brackets = {'{':'}', '(':')', '[':']'}
    active_brace = [value[0]]
    for c in value[1:]:
        if c in brackets:
            active_brace.insert(0, c)
        elif c != brackets[active_brace[0]]:
            return False
        else:
            active_brace.pop(0)
    if len(active_brace) != 0:
        return False
    return True