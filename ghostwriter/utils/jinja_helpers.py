def raw_file(filename: str) -> str:
    with open(filename) as f:
        x = f.read()
    return x
# end raw_file
# cfg['cat_file'] = raw_file