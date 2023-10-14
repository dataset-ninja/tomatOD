Dataset **tomatOD** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/8/5/K4/cwUbJIw8gmY0yRp3LjXmME62tRIOHKDSGfIe5VcKwYhI6w4ZBvOVgmeUaFIZ5jUxhNhBu8PT6ZwjAsd2RnFkJBQxuQL5MgYO8jhbPFxJE9SB7V8q5Bwq9xojvUlI.tar)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='tomatOD', dst_dir='~/dataset-ninja/')
```
Make sure not to overlook the [python code example](https://developer.supervisely.com/getting-started/python-sdk-tutorials/iterate-over-a-local-project) available on the Supervisely Developer Portal. It will give you a clear idea of how to effortlessly work with the downloaded dataset.

The data in original format can be downloaded here:

- [Images](https://datasets-u2m.s3.eu-west-3.amazonaws.com/tomatOD_images.zip)
- [Bounding box annotations (train and validation sets)](https://datasets-u2m.s3.eu-west-3.amazonaws.com/tomatOD_annotations.zip)
