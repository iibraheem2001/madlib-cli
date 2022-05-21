
with open('assets/short_example.txt') as f:
    contents = f.read()
    user_input = []

    # adj1 = input('enter an adjective')
    user_input.append(adj1)
    # adj2 = input('enter a second adjective')
    user_input.append(adj2)
    # noun1 = input('enter a noun')
    user_input.append(noun1)
    print(contents.format(*user_input))


