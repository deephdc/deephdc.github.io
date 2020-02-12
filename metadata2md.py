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
Category: {{ keywords|join(',') }}
GitHub: {{ sources.code }}
DockerHub: {{ sources.docker_registry_repo }}
{% if training_files_url is defined %}
Training_files: {{ training_files_url }}
{% endif %}
{% if cite_url is defined %}
Cite: {{ cite_url }}
{% endif %}
{% if dataset_url is defined %}
Dataset: {{ dataset_url }}
{% endif %}
License: {{ license }}
Summary: {{ summary }}
Slug: {{sources.docker_registry_repo.split("/")[1].replace("_", "-")}}
---
{% if continuous_integration is defined %}
[![Build Status]({{ continuous_integration.build_status_badge }})]({{ continuous_integration.build_status_url }})
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
                        help='Target markdown file')
    args = parser.parse_args()

    json_data = json.load(args.metadata)
    mtime = os.stat(args.metadata.name).st_mtime
    mtime_str = datetime.fromtimestamp(mtime).strftime('%Y-%m-%d %H:%M:%S')
    json_data['date_modification'] = mtime_str

    jinja_env = Environment(loader=BaseLoader()).from_string(TEMPLATE)
    md_data = jinja_env.render(json_data)
    if args.output_file:
        dirn = os.path.dirname(args.output_file)
        if not os.path.exists(dirn):
            os.makedirs(dirn)
        with open(args.output_file, 'w') as f:
            f.write(md_data)
    else:
        print(md_data)


if __name__ == "__main__":
    main()
