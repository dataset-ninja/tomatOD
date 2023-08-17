Dataset **tomatOD** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/I/6/NB/6zcncLtEjLI75wbOOMBIeFsExJbiIrrQWnrJgtrCRVQ0KkHU7tiXIitivlCle9JbkYiw87dQULOj7NdDvIyaVzLV9zGTIvVdT8r2GsB43yJcFNM0EGydKj8J3BAv.tar)

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
