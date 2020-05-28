import argparse
import sys
from textwrap import dedent


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

    # Output root directory. This will be reassigned at the end based on the
    # PATH argument.
    o_help = dedent('''\
        Output root directory for rendered templates. Defaults to PATH, i.e.
        rendered templates will appear in the same directory as their unrendered
        versions. The output root will propogate down the rendered tree; for
        example, if all your templates live in the top-level 'templates'
        directory, and that directory tree is the same structure as what SHOULD
        appear starting at project root, setting this to '.' will render
        all templates found under PATH and fill your project directory as though
        filled manually, without template clutter.''')
    parser.add_argument('-o', '--output-root',
                        help = o_help,
                        default = None)

    # Template pattern
    p_help = dedent('''\
        Filename pattern for template files. The default is '.gw'. The pattern
        must appear before any potential filename extension. For example, if a
        file is typically named 'file.json', then the file ghostwriter will
        render would be 'file.gw.json'. Setting this option to, for example,
        '_jinja' would force ghostwriter to instead render a file named
        'file_jinja.json'. Files that typically do not have an extension instead
        must end in this pattern, e.g. 'Dockerfile.gw'.''')
    parser.add_argument('-p', '--template-pattern',
                        help = p_help,
                        default = '.gw')
    
    # Add files to gitignore
    gitignore_help = dedent('''\
        Append the OUTPUT_DIR rendered to the '.gitignore' file found at the
        root of OUTPUT_DIR. Default behavior is to not alter that '.gitignore'.
        This option is useful if rendered output contains secrets, OR if the
        developer wants to avoid committing non-rendered files to ensure edits
        are only made to template files.''')
    parser.add_argument('-i', '--gitignore-rendered',
                        help = gitignore_help,
                        action = 'store_true',
                        default = False)

    # PATH
    path_help = dedent('''\
        Path to look for template files. Passing the -r/--recursive flag will
        recurse down the provided path. If the -n/--no-recursive flag is passed,
        ghostwriter will only render the top-level of the provided directory,
        or the single file provided.''')
    parser.add_argument('PATH', help = path_help)

    # Finalize
    args_out = parser.parse_args(args)
    
    # Reassign output directory to PATH if not set
    if args_out.output_root is None:
        args_out.output_root = args_out.PATH

    # Convert args `Namespace` object to dictionary
    args_dict = vars(args_out)

    return {'args': args_out, 'args_dict': args_dict}
# end parse_args


# CLI entrypoint, to debug --help, for example
if __name__ == '__main__':
    args = parse_args(sys.argv[1:])['args']
