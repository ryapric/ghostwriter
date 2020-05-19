from ghostwriter.cli.argparser import parse_args
from jinja2 import Template
import os
import sys
import yaml


def render(**kwargs):
    args = parse_args(sys.argv[1:])

    # Load user cfg
    with open(args['config_file']) as f:
        cfg = yaml.safe_load(f.read())

    # Get list of files

    # File to render is passed as arg 1 on CLI
    argfile = args['']
    print(f'Rendering {argfile}')

    # Please stick to the format, folks, I'm only one guy over here
    if '.gw' not in argfile:
        raise Exception('You may only pass in files containing `.gw` for rendering. Aborting.')

    # Read the file to render
    with open(argfile) as f:
        template = f.read()

    # Stick a do-not-edit header on top
    # lol jk, append to .gitignore instead
    header = """\
    #######################################################
    # !!! DO NOT EDIT BY HAND. Created by ghostwriter !!! #
    #######################################################

    """
    if '.json' not in argfile:
        template = header + template

    # Render Jinja template using global cfg dict
    jinja_template = Template(template)
    rendered_template = jinja_template.render(cfg = cfg)

    # Write back out!
    outfile = argfile.replace('.gw', '')
    with open(outfile, 'w') as f:
        f.write(rendered_template)
# end render
