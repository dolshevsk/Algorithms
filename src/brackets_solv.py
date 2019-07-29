def brackets(array):
    stack = []
    index_stack = []
    open_brackets = {'(':')','{':'}','[':']'}
    for i, el in enumerate(array,1):
        if el in open_brackets:
            stack.append(el)
            index_stack.append(i)
        elif not stack:
            if el in open_brackets.values():
                return i
        else:
            if el in open_brackets.values():
                top = stack.pop()
                index = index_stack.pop()
                if open_brackets[top]!=el:
                    return i
    return 'Success' if not stack and array else index_stack[0]
