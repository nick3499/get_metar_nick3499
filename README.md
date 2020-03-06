# get_metar_nick3499

Get decoded METAR data: Python3: subprocess.run(), click

![screen capture](screen_capture.png)

## Tested Using:

- Linux 5.4.0-14-generic
- Ubuntu 20.04 LTS (Focal Fossa)
- Python 3.8.2
- GNOME Shell 3.35.91

## Methods Used

- `subprocess.run()`
- `fire.Fire()`
- `click` methods

## Run get_metar_click.py

To run `get_metar_click.py` in Bash (Unix shell), save the following into a shell script and execute it:


```shell
/bin/python3 $HOME/scripts/get_metar/get_metar_click.py --station $1
```

Or run the raw script from Github in Bash to get the help doc:

```shell
$ curl -s https://raw.githubusercontent.com/nick3499/get_metar_nick3499/master/get_metar_click.py | python3
```

## Run get_metar_fire.py

To run `get_metar_fire.py` in Bash (Unix shell), save the following into a shell script and execute it:

```shell
/bin/python3 $HOME/scripts/get_metar/get_metar_fire.py $1
```

Or run the raw script from Github in Bash to get the help doc:

```shell
$ curl -s https://raw.githubusercontent.com/nick3499/get_metar_nick3499/master/get_metar_fire.py | python3
```

## Shebang Line

```python
#! /bin/python3
```

>The shebang is actually a human-readable instance of a magic number in the executable file, the magic byte string being 0x23 0x21, the two-character encoding in ASCII of #!. This magic number is detected by the "exec" family of functions, which determine whether a file is a script or an executable binary. The presence of the shebang will result in the execution of the specified executable, usually an interpreter for the script's language.

[Shebang_(Unix): Magic number: Wikipedia](https://en.wikipedia.org/wiki/Shebang_(Unix)#Magic_number)

## Imports (click version)

```python
from subprocess import run
import click
```

- `subprocess.run()` is used to execute command line args from a Python script in the Bash (Unix shell).
- `click` is used to generate command line interfaces.

## Imports (fire version)

```python
from subprocess import run
from fire import Fire
```

- `subprocess.run()` is used to execute command line args from a Python script in the Bash (Unix shell).
- `fire.Fire()` is used to generate command line interfaces.

## _get_data

```python
def _get_data(icao_code):
    return run(['curl',
                'ftp://tgftp.nws.noaa.gov/data/observations/metar/decoded/' +
                icao_code], check=True)
```

`_get_data` uses the `subprocess.run()` method to run command line args in the Bash (Unix shell). `curl` is used to get decoded METAR data from a `noaa.gov` FTP link. `icao_code` can be one of four ICAO codes depending on which specific airport is selected.

>If _check_ is true, and the process exits with a non-zero exit code, a CalledProcessError exception will be raised. Attributes of that exception hold the arguments, the exit code, and stdout and stderr if they were captured.

[subprocess — Subprocess management: Using the subprocess Module](https://docs.python.org/3/library/subprocess.html#using-the-subprocess-module)

## Click Group

```python
@click.group()
@click.option('--station/--no-station', default=False)
def get_decoded_metar(station):
```

The grouped commands are then bound to `get_decoded_metar()` using the `click.command()` method.

## Get METAR (click version)

```python
@get_decoded_metar.command()
def mor():
    '''Get decoded METAR data for Morris Municipal Airport.'''
    _get_data('KC09.TXT')

@get_decoded_metar.command()
def dbq():
    '''Get decoded METAR data for Dubuque Regional Airport.'''
    _get_data('KDBQ.TXT')

@get_decoded_metar.command()
def dvn():
    '''Get decoded METAR data for Davenport Municipal Airport.'''
    _get_data('KDVN.TXT')

@get_decoded_metar.command()
def pia():
    '''Get decoded METAR data for Peoria International Airport.'''
    _get_data('KPIA.TXT')
```

## Get METAR (fire version)

```python
def mor():
    '''Get decoded METAR for Morris Municipal Airport.'''
    _get_data('KC09.TXT')

def dbq():
    '''Get decoded METAR for Dubuque Regional Airport.'''
    _get_data('KDBQ.TXT')

def dvn():
    '''Get decoded METAR for Davenport Municipal Airport.'''
    _get_data('KDVN.TXT')

def pia():
    '''Get decoded METAR for Peoria International Airport.'''
    _get_data('KPIA.TXT')
```

## if __name__ == '__main__' (click version)

```python
if __name__ == '__main__':
    get_decoded_metar()
```

If executed as a standalone app, `get_decoded_metar()` will run automatically. Otherwise, if imported into another module, its name will no longer be main, and dot syntax will be required to start it.

## if __name__ == '__main__' (fire version)

```python
if __name__ == '__main__':
    Fire()
```
