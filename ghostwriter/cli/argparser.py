import argparse
import sys


def parse_args(args):
    parser = argparse.ArgumentParser()

    # Config file
    parser.add_argument('-c', '--config-file',
                        help = 'ghostwriter YAML config file',
                        default = 'ghostwriter.yaml')

    # PATH recursion options are mutually-exclusive
    recursive_group = parser.add_mutually_exclusive_group()
    recursive_group.add_argument('-r', '--recursive',
                                help = 'Recurse directory tree of PATH (default behavior)',
                                action = 'store_const',
                                dest = 'recursive',
                                const = True,
                                default= True)
    recursive_group.add_argument('-n', '--no-recursive',
                                help = 'Do not recurse directory tree of PATH',
                                action = 'store_const',
                                dest = 'recursive',
                                const = False)

    # Output root directory
    parser.add_argument('-o', '--output-root',
                        help = '',
                        default = '.')
    
    # Template pattern
    t_help = '''
    Filename pattern for template files. The default is '.gw'. The pattern must
    appear before any potential filename extension. For example, if a file is
    typically named 'file.json', then the file ghostwriter will render would be
    'file.gw.json'. Setting this option to, for example, '_jinja' would force
    ghostwriter to instead render a file named 'file_jinja.json'. Files that
    typically do not have an extension instead must end in this pattern, e.g.
    'Dockerfile.gw'.
    '''
    parser.add_argument('-t', '--template-pattern',
                        help = t_help,
                        default = '.gw')

    # PATH
    path_help = '''
    Path to look for template files. Passing the -r/--recursive flag will
    recurse down the provided path. If the -n/--no-recursive flag is passed,
    ghostwriter will only render the top-level of the provided directory,
    or the single file provided.
    '''
    parser.add_argument('PATH', help = path_help)

    # Finalize
    args_out = parser.parse_args(args)
    args_dict = vars(args_out)

    return {'args': args_out, 'args_dict': args_dict}
# end parse_args


# CLI entrypoint, to debug --help, for example
if __name__ == '__main__':
    args = parse_args(sys.argv[1:])['args']
