from collections import OrderedDict


# A(B(DF))
def build_tree(input):
    n, tree, i = len(input), OrderedDict(), 0
    while i < n - 1:
        if input[i] not in '()' and input[i + 1] not in '()':
            tree[input[i]] = '#'
            i += 1
        elif input[i] not in '()' and input[i + 1] in '(':
            end = find_end(input, i + 1)
            tree[input[i]] = build_tree(input[i+2: end])
            i = end + 1
    if i == n - 1 and input[i] not in '()':
        tree[input[i]] = '#'
    return tree


def find_end(input, i):
    bracket = 1
    for i in range(i + 1, len(input)):
        if input[i] in '(':
            bracket += 1
        elif input[i] in ')':
            bracket -= 1
        if bracket == 0:
            return i


if __name__ == '__main__':
    input = 'A(B(DF)GH)IJ'
    tree = build_tree(input)
    print(tree)

