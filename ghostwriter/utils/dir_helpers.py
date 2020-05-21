import os


def build_tree(path, pattern = None):
    tree = []
    for root, _, filenames in os.walk(path):
        for f in filenames:
            tree.append(os.path.join(root, f))
    if pattern is not None:
        tree = [x for x in tree if pattern in x]
    
    # Bad pattern results in empty list, so throw an error
    if len(tree) > 0:
        return tree
    else:
        raise Exception(f"Searching for pattern '{pattern}' on path '{path}' yielded no file results")
# end build_tree


def gitignore_rendered(output_root):
    gitignore_path = os.path.abspath('.gitignore')

    # Return early if no gitignore exists
    try:
        with open(gitignore_path, 'r') as f:
            content = f.read()
    except FileNotFoundError:
        return

    header = '\n\n### GHOSTWRITER AUTOIGNORES, DO NOT WRITE BELOW THIS LINE ###\n'
    if header not in content:
        content += header

    if output_root not in content:
        content += output_root + '\n'

    with open(gitignore_path, 'w') as f:
        f.write(content)
# end gitignore_rendered


def read_file(path):
    with open(path) as f:
        content = f.read()
    return content
# end read_file
