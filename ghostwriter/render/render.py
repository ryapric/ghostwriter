#!/usr/bin/env python3

"""
This script is the workhorse that safely fills all of the dynamic values across
all files in this repo.
"""

from jinja2 import Template
import sys
import yaml

# Load user cfg
with open('./ghostwriter.yaml') as f:
    cfg = yaml.safe_load(f.read())

# Define any helper functions you might want to pass to templates to use
def raw_file(filename):
    with open(filename) as f:
        x = f.read()
    return x
cfg['cat_file'] = cat_file

# File to render is passed as arg 1 on CLI
argfile = sys.argv[1]
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
