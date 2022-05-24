def read_template(path):
    with open(path) as f:
        return f.read()

def parse_template(template):
    stripped = ""
    parts = []
    captured_string = ""
    capturing = False
    for char in template:
        if capturing:
            if char == "}":
                capturing = False
                parts.append(captured_string)
                captured_string = ""
                stripped += char
            else: captured_string += char
        else:
            stripped += char
            if char == "{":
                capturing = True
    return [stripped, tuple(parts)]



def merge(stripped_string, user_input):
    final_string = stripped_string.format(*user_input)
    return final_string


    # txt3 = "My name is {}, I'm {}".format("abe", 20)

# user_input = []

# adj1 = input('enter an adjective')
# user_input.append(adj1)
# adj2 = input('enter a second adjective')
# user_input.append(adj2)
# noun1 = input('enter a noun')
# user_input.append(noun1)
# print(contents.format(*user_input))


