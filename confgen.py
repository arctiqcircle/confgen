#!/usr/bin/env python3

import logging
import os
import sys

import jinja2
import yaml
import csv
import argparse

# Set Up Logging
directory = os.getcwd()
logging_file = os.path.join(directory, "configgen.log")
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger()
file_handler = logging.FileHandler(logging_file)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)
logger.setLevel(logging.DEBUG)


def unpack(filename: str) -> list[dict]:
    """
    unpack unpacks a YAML or CSV into a list of dictionaries
    :param filename: the filename containing the data
    :return: a list of dictionaries
    """
    unpacked = []
    rel_path = os.path.join(directory, filename)
    with open(rel_path, 'r') as f:
        if filename.endswith(".csv"):
            reader = csv.DictReader(f)
            for row in reader:
                for field, value in row.items():
                    if value.endswith(".csv"):
                        rel_spath = os.path.join(directory, value)
                        sdata = []
                        with open(rel_spath, 'r') as f:
                            sreader = csv.DictReader(f)
                            for srow in sreader:
                                sdata.append(srow)
                        row[field] = sdata
                unpacked.append(row)
        elif filename.endswith(".yml") or filename.endswith(".yaml"):
            unpacked = yaml.load(f, yaml.BaseLoader)
    return unpacked


def read_template(filename: str) -> jinja2.Template:
    """
    read_template reads a file into a jinja2 Template
    :param filename: the filename containing the template
    :return: a Template with the contents of the file
    """
    with open(filename, 'r') as f:
        template_text = f.read()
    return jinja2.Template(template_text)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Generate a configuration from J2 template")
    parser.add_argument("-d", dest="data", default=None, help="data filename (CSV or YAML)")
    parser.add_argument("-t", dest="template", default=None, help="template filename (j2)")
    opts = parser.parse_args(args=sys.argv[1:])
    data = []
    template: jinja2.Template = None
    if opts.data:
        try:
            data = unpack(opts.data)
        except Exception as e:
            logger.error(e)
    else:
        logging.error("no data file provided")
    if opts.template:
        try:
            template = read_template(opts.template)
        except Exception as e:
            logger.error(e)
    else:
        logging.error("no template file provided")
    for entry in data:
        render = template.render(entry)
        path = os.path.join(directory, f"{entry['name']}.conf")
        with open(path, 'w') as f:
            f.write(render)
