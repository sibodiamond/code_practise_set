from collections import deque
import bisect


class TreeNode:
    def __init__(self, v):
        self.val = v
        self.left = None
        self.right = None


# {'A':3, 'B':2, 'C':4}
def build_haffman_tree(freq):
    freq_sorted = sorted(freq.items(), key=lambda x: x[1])
    freqs = deque([pair[1] for pair in freq_sorted])
    nodes = deque([TreeNode(pair[0]) for pair in freq_sorted])
    while len(freqs) > 1:
        f1 = freqs.popleft()
        f2 = freqs.popleft()
        node1 = nodes.popleft()
        node2 = nodes.popleft()
        new_node = TreeNode(None)
        if f1 < f2:
            new_node.left, new_node.right = node1, node2
        else:
            new_node.left, new_node.right = node2, node1
        li = bisect.bisect_left(freqs, f1 + f2)
        bisect.insort_left(freqs, f1 + f2)
        nodes.insert(li, new_node)
        freq_sorted.insert(li, (None, f1 + f2))
    return nodes[-1]


def create_encoded_mapping(node):
    res = {}

    def dfs(node, path):
        if not node.left and not node.right:
            res[node.val] = path
        if node.left:
            dfs(node.left, path + '0')
        if node.right:
            dfs(node.right, path + '1')

    dfs(node, '')
    return res


if __name__ == '__main__':
    freq = {'A': 3, 'B': 2, 'C': 4, 'D': 5, 'E': 1, 'F': 6}
    t = build_haffman_tree(freq)
    res = create_encoded_mapping(t)
    print(res)


