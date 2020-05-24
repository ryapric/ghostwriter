import ghostwriter.cli.argparser as ap
import pytest
import subprocess

def test_parse_args():
    # Defaults
    args = '.'.split()
    args_dict = ap.parse_args(args)['args_dict']
    assert args_dict['PATH'] == '.'
    assert args_dict['config_file'] == 'ghostwriter.yaml'
    assert args_dict['recursive']
    assert args_dict['template_pattern'] == '.gw'
    assert args_dict['output_root'] == args_dict['PATH']
    assert args_dict['gitignore_rendered'] == False

    # Different PATH (not a default though)
    args = 'input'.split()
    args_dict = ap.parse_args(args)['args_dict']
    assert args_dict['PATH'] == 'input'

    # Recursive
    args = '-r .'.split()
    args_dict = ap.parse_args(args)['args_dict']
    assert args_dict['PATH'] == '.'
    assert args_dict['recursive']

    # Not recursive
    args = '-n .'.split()
    args_dict = ap.parse_args(args)['args_dict']
    assert args_dict['PATH'] == '.'
    assert not args_dict['recursive']

    # Both recursive options throw an error
    args = '-r -n .'.split()
    with pytest.raises(SystemExit):
        args_dict = ap.parse_args(args)['args_dict']
    
    # Output root directory
    args = '-o output_dir .'.split()
    args_dict = ap.parse_args(args)['args_dict']
    assert args_dict['output_root'] == 'output_dir'

    # Template pattern
    args = '-t _jinja .'.split()
    args_dict = ap.parse_args(args)['args_dict']
    assert args_dict['template_pattern'] == '_jinja'

    # Append PATH to working-directory .gitignore
    args = '-i .'.split()
    args_dict = ap.parse_args(args)['args_dict']
    assert args_dict['gitignore_rendered'] == True

# end test_parse_args


def test_main():
    # Run external shell script for integration testing
    results = subprocess.run(
        'bash tests/test-cli-installed.sh'.split(),
        capture_output = True)
    # stdout is bytes, for some reason
    print(results.stdout.decode('utf8'))
    # WHY ISN'T THAT PRINTING
    raise Exception
    
    # This throws a CalledProcessError if the exit code wasn't 0
    results.check_returncode
# end test_main
