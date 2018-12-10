# pptx-template [![Build Status](https://cloud.drone.io/api/badges/skar404/pptx-template/status.svg)](https://cloud.drone.io/skar404/pptx-template)

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

## Getting started

```bash
pip install pptx-template-fork
```

### Python: 
```python
from pptx import Presentation
from pptx_template.cli import process_all_slides

ppt = Presentation('in.pptx')
process_all_slides({
        "0": "remove",
        "1": {
            "greeting": {
                "en": "Hello!",
                "ja": "こんにちは！"
            },
            "season": ["Spring", "Summer", "Autumn", "Winter"]
        },
}, ppt, True)
ppt.save('out.pptx')
```


### CLI: 

```bash
echo '{ "slides": [ { "greeting" : "Hello!!" } ] }' > model.json

# prepare your template file (test.pptx) which contains "{greeting}" in somewhere

pptx-template --out out.pptx --template test.pptx --model model.json
```
