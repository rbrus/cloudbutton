import os
import click
import logging
import cloudbutton.engine as eng
from cloudbutton.cli.runtime.cli import runtime
from cloudbutton.cli import clean_all
from cloudbutton.engine.tests import print_help, run_tests


def set_debug(debug):
    if debug:
        logging.basicConfig(level=logging.DEBUG)
        os.environ["CLOUDBUTTON_LOGLEVEL"] = 'DEBUG'


@click.group()
def cli():
    pass


@cli.command('clean')
def clean():
    set_debug(True)
    clean_all()


@cli.command('test')
@click.option('--debug', '-d', is_flag=True, help='debug mode')
def test_function(debug):
    set_debug(debug)

    def hello(name):
        return 'Hello {}!'.format(name)

    pw = eng.function_executor()
    pw.call_async(hello, 'World')
    result = pw.get_result()
    print()
    if result == 'Hello World!':
        print(result, 'Pywren is working as expected :)')
    else:
        print(result, 'Something went wrong :(')
    print()


@cli.command('verify')
@click.option('--test', '-t', default='all', help='run a specific test, type "-t help" for tests list')
@click.option('--config', '-c', default=None, help='use json config file')
@click.option('--debug', '-d', is_flag=True, help='debug mode')
def verify(test, config, debug):
    if test == 'help':
        print_help()
    else:
        set_debug(debug)
        run_tests(test, config)


cli.add_command(runtime)

if __name__ == '__main__':
    cli()
