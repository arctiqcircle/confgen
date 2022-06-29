# ConfGen
 > A simple Jinaj2 rendering script for generating configurations fro CSV or YAML data.

## Getting Started
To use ConfGen you're going to need to install a couple of programs and libraries.

- For Windows, Download Git for Windows at gitforwindows.org
- For Mac and Linux, follow instructions at git-scm.com
- Install Python 3 from python.org
- Install the required Python Libraries via pip

```shell
python3 -m pip install -r requirements.txt
```

### Installation

To install ConfGen we'll be using git to download this repository.

* Do a git clone of this repository into a directory of your choosing
```shell
git clone https://github.com/dyntek-services-inc/confgen.git
```

### Operation

To run ConfGen you'll need at least two files, a data file and a template file,
in your current working directory. The data file can be defined in CSV or YAML format.
CSV documents support nested documents. See [tests/data/data.csv](tests/data/data.csv)
for an example. Template files should be defined according to the
[Jinja2](https://jinja.palletsprojects.com/en/3.1.x/) templating language.

You run ConfGen at the command-line like so;
```shell
python3 confgen.py -d tests/data/data.csv -t tests/templates/template.j2
```

## Authors

***Kenneth J Grace*** - *Initial Work* - [KennethGrace](https://github.com/KennethGrace)

## License

This project is licensed under the MIT License - see the [LICENSE.txt](LICENSE.md) file for details