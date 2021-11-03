from ghostwriter.render.render import render
from ghostwriter.utils.dir_helpers import build_tree, read_file
import os
import pytest
from textwrap import dedent


def test_render():
    args_dict = {
        'config_file': 'tests/ghostwriter.yaml',
        'PATH': 'tests/test_path'
    }
    render(**args_dict)
    want = "postgresql://postgres:password@some-host:5432"
    got = read_file('tests/test_path/db.txt')
    assert want == got


# end test_render

def test_cleanup():
    tree = build_tree('tests/test_path')
    tree = [x for x in tree if '.gw' not in x and '.gitignore' not in x]
    for f in tree:
        try:
            os.remove(f)
        except IsADirectoryError:
            os.rmdir(f)
        finally:
            pass
 # end cleanup
