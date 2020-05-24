from ghostwriter.utils.dir_helpers import build_tree
import os
import pytest


def test_build_tree():
    # Default option finds all files
    got = build_tree('tests/test_dir_helpers')
    want = [os.path.join('tests', 'test_dir_helpers', x) for x in ['file.txt', 'file.gw.txt']]
    assert got == want

    # `pattern` filters result set to files containing the pattern
    got = build_tree('tests/test_dir_helpers', pattern = '.gw')
    want = [os.path.join('tests', 'test_dir_helpers', 'file.gw.txt')]
    assert got == want

    # Bad pattern should return empty list, which is an error
    with pytest.raises(Exception):
        build_tree('tests/test_dir_helpers', pattern = 'not_real')
    
    # Recursive options should be respected
    raise Exception
# end test_build_tree


def test_gitignore_rendered():
    raise Exception
# end test_gitignore_rendered


def test_read_file():
    raise Exception
# end test_read_file
