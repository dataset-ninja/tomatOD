Dataset **tomatOD** can be downloaded in Supervisely format:

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/0/r/Z5/bb7R0aaqwow9YDsScIynpUUHRgxT11hvqCU3hMTOGve4BLOgQEtXum2oni5vPVbo88VhLK54WLxwUotooGjVtqhJfe6JfQqqRAtOmtrK3ep5MqB2gXOWkYFMusJh.tar)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='tomatOD', dst_path='~/dtools/datasets/tomatOD.tar')
```
The data in original format can be downloaded here:

- 🔗[Images](https://datasets-u2m.s3.eu-west-3.amazonaws.com/tomatOD_images.zip)
- 🔗[Bounding box annotations (train and validation sets)](https://datasets-u2m.s3.eu-west-3.amazonaws.com/tomatOD_annotations.zip)
