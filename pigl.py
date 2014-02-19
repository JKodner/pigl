def convert(x):
    suffix = "ay"
    if len(x) > 0:
        if x[0] in "aeiou":
            new_word = x + suffix
        else:
            new_word = x[1:] + x[0].lower() + suffix
    return new_word.title()

