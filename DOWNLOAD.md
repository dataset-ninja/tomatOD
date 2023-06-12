Dataset **TomatOD** can be downloaded in Supervisely format:

 [Download](https://assets.supervise.ly/supervisely-supervisely-assets-public/teams_storage/3/E/jT/ZYpX9f7tkdaXWsjrfh0h98q8R8nTRF5PmKli3ly4pPN3Va7rWRKKoWJvjb1XKjbzYfNNynnPj8vDKVmp4lT1Nl8qdOnMK9k6VHWzxLZ7W0ps7efCbqdqJnDB7Wvt.tar)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='TomatOD', dst_path='~/dtools/datasets/TomatOD.tar')
```
The data in original format can be downloaded here:

- 🔗[Images](https://datasets-u2m.s3.eu-west-3.amazonaws.com/tomatOD_images.zip)
- 🔗[Bounding box annotations (train and validation sets)](https://datasets-u2m.s3.eu-west-3.amazonaws.com/tomatOD_annotations.zip)
