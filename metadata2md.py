#!/usr/bin/env python

import argparse
from datetime import datetime
import os

from jinja2 import Environment, BaseLoader
import simplejson as json


TEMPLATE = '''
---
Title: {{ title }}
Date: {{ date_creation }}
Modified: {{ date_modification }}
Category: {{ keywords }}
GitHub: {{ sources.code }}
DockerHub: {{ sources.docker_registry_repo }}
Training_files: {{ training_files_url | default('NA') }}
License: {{ license }}
Summary: {{ summary }}
---
{% if continuous_integration is defined %}
[![Build Status]({{ continuous_integration.build_status_badge }})](continuous_integration.build_status_url)
{% endif %}

{{ description | join('\n') }}
{% if description_references is defined %}
**References**"
{{ description_references }}
{% endif %}
'''

def main():
    parser = argparse.ArgumentParser(description=('Render DEEP application '
                                                  'metadata as Pelican '
                                                  'markdown document.'))
    parser.add_argument('metadata',
                        metavar='METADATA_JSON_FILE',
                        type=argparse.FileType('r'),
                        help='DEEP application metadata')
    parser.add_argument('--output-file',
                        metavar='MARKDOWN_FILE',
                        type=argparse.FileType('w'),
                        help='Target markdown file')
    args = parser.parse_args()

    json_data = json.load(args.metadata)
    mtime = os.stat(args.metadata.name).st_mtime
    mtime_str = datetime.fromtimestamp(mtime).strftime('%Y-%m-%d %H:%M:%S')
    json_data['date_modification'] = mtime_str

    jinja_env = Environment(loader=BaseLoader()).from_string(TEMPLATE)
    md_data = jinja_env.render(json_data)
    if args.output_file:
        args.output_file.write(md_data)
    else:
        print(md_data)

if __name__ == "__main__":
    main()
