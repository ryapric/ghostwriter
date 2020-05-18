import ghostwriter.cli.main as cli
import pytest

def test_parse_args():
    # Defaults
    args = '.'.split()
    args_dict = cli.parse_args(args)['args_dict']
    assert args_dict['PATH'] == '.'
    assert args_dict['recursive']
    assert args_dict['config_file'] == 'ghostwriter.yaml'

    # Different PATH (not a default though)
    args = 'input'.split()
    args_dict = cli.parse_args(args)['args_dict']
    assert args_dict['PATH'] == 'input'

    # Recursive
    args = '-r .'.split()
    args_dict = cli.parse_args(args)['args_dict']
    assert args_dict['PATH'] == '.'
    assert args_dict['recursive']

    # Not recursive
    args = '-n .'.split()
    args_dict = cli.parse_args(args)['args_dict']
    assert args_dict['PATH'] == '.'
    assert not args_dict['recursive']

    # Both recursive options throw an error
    args = '-r -n .'.split()
    with pytest.raises(SystemExit):
        args_dict = cli.parse_args(args)['args_dict']
    
    # Output root directory
    args = '-o output/ .'.split()
    args_dict = cli.parse_args(args)['args_dict']
    assert args_dict['output_root'] == 'output/'
# end test_parse_args
