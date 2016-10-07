from pelican.readers import BaseReader
from pelican import signals

import os
import json
import logging

import pypandoc

logger = logging.getLogger(__name__)


class PandocReader(BaseReader):
    enabled = True
    file_extensions = ['md']
    output_format = 'html5'

    METADATA_TEMPLATE = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                             'metadata.template')

    def read(self, filename):
        # Get meta data
        metadata = self.read_metadata(filename)

        # Get content
        self.process_settings()
        content = pypandoc.convert_file(filename, to=self.output_format, extra_args=self.extra_args, filters=self.filters)
        return content.encode('utf-8'), metadata

    def read_metadata(self, path, format=None):
        metadata_json = pypandoc.convert_file(path, to='markdown', format=format,
                                     extra_args=['--template', self.METADATA_TEMPLATE])

        _metadata = json.loads(metadata_json)
        metadata = dict()
        for key, value in _metadata.items():
            metadata[key] = self.process_metadata(key, value)

        return metadata

    def process_settings(self):
        self.extra_args = self.settings.get('PANDOC_ARGS', [])
        self.filters = self.settings.get('PANDOC_EXTENSIONS', []) 

def add_reader(readers):
    for ext in PandocReader.file_extensions:
        readers.reader_classes[ext] = PandocReader

def register():
    logger.debug("Registering pandoc_reader plugin.")
    signals.readers_init.connect(add_reader)
