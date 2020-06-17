# pptx-template

## Getting started

The goal of this fork is to provide a PyPI package that you can use in your
python project by calling the `pptx_template.render.render_pptx` function.

Some features provided by the originals projects
(https://github.com/skar404/pptx-template and https://github.com/m3dev/pptx-template)
may not work properly.

### Install

    pip3 install pptx_template_simple

In this fork, you can render a template like this:

```python
from pptx_template import render

input_path = 'test/data5/in.pptx'
model = {
    "greeting": "Hello!",
    "client_name": "M. Melpanque"
}
output_path = 'test/data5/out.pptx'
render.render_pptx(input_path, model, output_path)
```

## Development

Test manualy the package:

    python3 main.py

Install dependencies:

    sudo apt-get -y install python3-setuptools
    pip3 install wheel
    pip3 install twine

Build the package:

    python3 setup.py bdist_wheel

Install the local build package:

    pip3 install dist/pptx_template_simple-0.2.8-py3-none-any.whl

Upload to test pypi:

    twine upload --repository testpypi dist/*

Then test your package by installing the test pypi package:

    pip3 install --index-url https://test.pypi.org/simple/ --no-deps pptx_template_simple

When you are ready, upload the package in the main pypi repository:

    twine upload dist/*

### Tests

Install dependencies:

    pip3 install pytest

Run tests:

    pytest


### TODO

 - Substitute images
 - Use Jinja template syntax

## Overview

pptx-template is a PowerPoint presentation builder.

This helps your routine reporting work that have many manual copy-paste from excel chart to powerpoint, or so.

  - Building a new powerpoint presentation file from a "template" pptx file which contains "id"
  - Import some strings and CSV data which is defined in a JSON config file or a Python dict
  - "id" in pptx template is expressed as a tiny DSL, like "{sales.0.june.us}"
  - requires python envirionment (2 or 3), pandas, python-pptx
  - for now, only UTF-8 encoding is supported for json, csv

### Text substitution
!<img src="docs/01.png?raw=true" width="80%" />

### CSV Import
!<img src="docs/02.png?raw=true" width="80%" />

## Japanese translation

pptx-template は pptx のテンプレートを元に、別途用意した JSON 中の文字列や CSV データを差し込んだ pptx を生成するツールです。

定型レポートなどで大量のグラフ付きスライドを作成する際の作業を代行してくれます。

  - テンプレートには "{sales.0.june.us}" のような形で JSON内の値を指す id を記入できます
  - python 2 または 3, pandas, pptx に依存しています
  - 扱う json や csv の 文字コードは utf-8 前提です
