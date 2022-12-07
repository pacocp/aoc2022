class Tree:
    def __init__(self, name, parent=None):
        self.name = name
        self.children = []
        self.size = 0
        self.parent = parent
    def add_child(self, node):
        assert isinstance(node, Tree)
        self.children.append(node)
    def get_child_by_name(self, name):
        for child in self.children:
            if name == child.name:
                return child
        return None

def retrieve_all_sizes(tree):
    visited = []
    nonvisited = []
    for node in tree.children:
        nonvisited.append(node)
    all_sizes = []
    while nonvisited != []:
        node = nonvisited.pop()
        all_sizes.append(node.size)
        visited.append(node)
        for child in node.children:
            nonvisited.append(child)
    return all_sizes

def retrieve_root_node(actual_node):
    while actual_node.parent != None:
        actual_node = actual_node.parent

    return actual_node

def dir_to_delete(tree, free_space):
    visited = []
    nonvisited = []
    for node in tree.children:
        nonvisited.append(node)
    all_sizes = []
    while nonvisited != []:
        node = nonvisited.pop()
        if (free_space + node.size) >= 30000000:
            all_sizes.append(node.size)
        visited.append(node)
        for child in node.children:
            nonvisited.append(child)
    return min(all_sizes)

def part1(lines):
    actual_node = Tree('root', parent=None)
    for line in lines:
        if '$ cd /' in line: continue
        if '$ cd ..' in line:
           actual_node = actual_node.parent
        elif '$ cd' in line:
            dir_ = line.strip().split(' ')[-1]
            actual_node =  actual_node.get_child_by_name(dir_)
        elif '$ ls' in line:
            continue
        elif '$' not in line:
            value = line.strip().split(' ')[0]
            name = line.strip().split(' ')[1]
            if value != 'dir':
                actual_node.size += int(value)
                prev_node = actual_node.parent
                if prev_node:
                    prev_node.size += int(value)
                    while prev_node.parent != None:
                        prev_node = prev_node.parent
                        prev_node.size += int(value)
            elif value == 'dir':
                child = Tree(name, actual_node)
                actual_node.add_child(child)
    
    root_node = retrieve_root_node(actual_node)
    all_sizes = retrieve_all_sizes(root_node)
    all_sizes = [value for value in all_sizes if value <= 100000]
    return sum(all_sizes)

def part2(lines):
    actual_node = Tree('root', parent=None)
    for line in lines:
        if '$ cd /' in line: continue
        if '$ cd ..' in line:
           actual_node = actual_node.parent
        elif '$ cd' in line:
            dir_ = line.strip().split(' ')[-1]
            actual_node =  actual_node.get_child_by_name(dir_)
        elif '$ ls' in line:
            continue
        elif '$' not in line:
            value = line.strip().split(' ')[0]
            name = line.strip().split(' ')[1]
            if value != 'dir':
                actual_node.size += int(value)
                prev_node = actual_node.parent
                if prev_node:
                    prev_node.size += int(value)
                    while prev_node.parent != None:
                        prev_node = prev_node.parent
                        prev_node.size += int(value)
            elif value == 'dir':
                child = Tree(name, actual_node)
                actual_node.add_child(child)
    
    root_node = retrieve_root_node(actual_node)
    free_space = 70000000 - root_node.size
    return dir_to_delete(root_node, free_space)

with open('input.txt', 'r') as f:
    lines = f.readlines()
    sum_dirs = part1(lines)
    free_space = part2(lines)

print(f'Sum of files {sum_dirs}')
print(f'Size of dir to delete {free_space}')
