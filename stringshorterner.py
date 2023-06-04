def split_string(string, split_length):
    words = string.split()
    splits = []
    current_split = ''

    for word in words:
        if len(current_split) + len(word) <= split_length:
            current_split += word + ' '
        else:
            splits.append(current_split.strip())
            current_split = word + ' '

    if current_split:
        splits.append(current_split.strip())

    return splits

def split_string_down_line(string, split_length):
    words = string.split()
    splits = []
    current_split = ''

    for word in words:
        if len(current_split) + len(word) <= split_length:
            current_split += word + ' '
        else:
            splits.append(current_split.strip())
            current_split = word + ' '

    if current_split:
        splits.append(current_split.strip())

    return '\n'.join(splits)



def split_string_length(string, line_length):
    words = string.split()
    lines = []
    current_line = ''
    current_length = 0

    for word in words:
        word_length = len(word)

        if current_length + len(current_line) + word_length + 1 <= line_length:
            current_line += word + ' '
            current_length += word_length + 1
        else:
            lines.append(current_line.strip())
            current_line = word + ' '
            current_length = word_length + 1

    if current_line:
        lines.append(current_line.strip())

    return '\n'.join(lines) + '\n'
