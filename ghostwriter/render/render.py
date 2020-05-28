from ghostwriter.cli.argparser import parse_args
from ghostwriter.utils.dir_helpers import gitignore_rendered, build_tree
from jinja2 import Template
import os
import yaml


def render(**kwargs):
    # We need to dummy up the args dictionary as though the entries were the
    # command-line args
    cli_args = []
    for k, v in kwargs.items():
        if k == 'PATH':
            continue
        k_fixed = f"--{k.replace('_', '-')}"
        args_i = ' '.join([k_fixed, str(v)])
        cli_args.append(args_i)
    # end for
    cli_args = f"{cli_args[0]} {kwargs['PATH']}".split()
    
    args = parse_args(cli_args)['args_dict']

    # Load user cfg
    with open(args['config_file']) as f:
        cfg = yaml.safe_load(f.read())

    # Get list of files
    tree = build_tree(
        args['PATH'],
        pattern = args['template_pattern'],
        recursive = args['recursive']
    )

    for pathfile in tree:
        print(f'Rendering {pathfile}...')

        # Read the file to render
        with open(pathfile) as f:
            template = f.read()

        # Render Jinja template using global cfg dict
        jinja_template = Template(template)
        rendered_template = jinja_template.render(cfg = cfg)

        # Write back out!
        outfile = pathfile.replace(args['template_pattern'], '')

        with open(outfile, 'w') as f:
            f.write(rendered_template)
    # end for
    
    if args['gitignore_rendered']:
        gitignore_rendered(os.path.relpath(args['output_root']))
# end render
