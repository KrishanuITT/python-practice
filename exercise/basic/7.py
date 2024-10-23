# Find no of occurrence of a substring:

str_x = "Krishanu is good developer. Krishanu is a writer"

def count_substring(string, sub_string):
    return f"{sub_string} occurs {len([i for i in range(len(string)) if string.startswith(sub_string, i)])} times"

print(count_substring(str_x, "Krishanu"))