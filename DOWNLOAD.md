Dataset **tomatOD** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/remote/eyJsaW5rIjogInMzOi8vc3VwZXJ2aXNlbHktZGF0YXNldHMvMTM0N190b21hdE9EL3RvbWF0b2QtRGF0YXNldE5pbmphLnRhciIsICJzaWciOiAiN2xsb1kwMlQ0VGRWL09kSFRUVW9kbHpscUlhQ3VXNFo5L2haejdRSUR4dz0ifQ==?response-content-disposition=attachment%3B%20filename%3D%22tomatod-DatasetNinja.tar%22)

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
