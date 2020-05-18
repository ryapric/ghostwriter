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


    # PATH
    path_help = '''
    Path to look for template files. Passing the -r/--recursive flag will recurse
    down the provided path.
    '''
    parser.add_argument('PATH', help = path_help)


    # Finalize
    args_out = parser.parse_args(args)
    args_dict = vars(args_out)

    return {'args': args_out, 'args_dict': args_dict}
# end parse_args


# Main
def main(args_dict):
    print(args_dict)

if __name__ == '__main__':
    main(parse_args(sys.argv[1:])['args_dict'])
