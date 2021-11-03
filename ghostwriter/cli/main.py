from ghostwriter.cli.argparser import parse_args
from ghostwriter.render.render import render
import sys

def main() -> None:
    parsed = parse_args(sys.argv[1:])
    # args = parsed['args']
    args_dict = parsed['args_dict']
    render(**args_dict)

if __name__ == '__main__':
    main()
