This README isn't fully true yet; just a placeholder for features until I add
them to GH Issues or something.

ghostwriter
===========

Generate code, config, IaC, and more from template files -- all using a single
master config file

Very similar to [HasiCorp Consul
Template](https://github.com/hashicorp/consul-template), but does not rely on
another service to manage the config values for you.

Installation
------------

`ghostwriter` is distributed as a Python package, so can be installed with
`pip`:

    pip3 install -U ghostwriter

Usage
-----

Assuming your master config is called `ghostwriter.yaml`, the following will
render all templates, recursively, in the current directory

    ghostwrite -c ghostwriter.yaml -r .

Template files default to being named the same as their output file, with the
`.gw` extension *before* their actual extension, e.g. `myfile.gw.txt`. You may
change the pattern that `ghostwriter` searches for using the `-t` switch (for
"template pattern"). Currently, only the notion of a pre-file extension is
supported, and not other pattern-matching algorithms.

`ghostwriter` defaults to writing out its templated files to the same directory
that it found a template in, with the correct file extension. You may also
specify the output directory for all rendered templates with the `-o` switch to
have it write to another directory. For example, if all your templates live in a
top-leve folder called `ghostwriter-templates`, and you want to have the results
populate your root directory tree, the following will accomplish that:

    ghostwrite -c ghostwriter.yaml -r -o . ghostwriter-templates/
