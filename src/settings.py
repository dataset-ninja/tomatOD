from typing import Dict, List, Optional, Union

from dataset_tools.templates import AnnotationType, CVTask, Industry, License

##################################
# * Before uploading to instance #
##################################
PROJECT_NAME: str = "tomatOD"
PROJECT_NAME_FULL: str = "tomatOD: Tomato Fruit Localization and Ripening Classification"

##################################
# * After uploading to instance ##
##################################
LICENSE: License = License.CC_BY_NC_SA_4_0()
APPLICATIONS: List[Industry] = [Industry.Agriculture()]
CV_TASKS: List[CVTask] = [CVTask.ObjectDetection()]
ANNOTATION_TYPES: List[AnnotationType] = [CVTask.ObjectDetection()]

RELEASE_YEAR: int = 2020
HOMEPAGE_URL: str = "https://github.com/up2metric/tomatOD"
# e.g. "https://some.com/dataset/homepage"

PREVIEW_IMAGE_ID: int = 1633599
# This should be filled AFTER uploading images to instance, just ID of any image.

GITHUB_URL: str = "https://github.com/dataset-ninja/tomatOD"
# URL to GitHub repo on dataset ninja (e.g. "https://github.com/dataset-ninja/some-dataset")

##################################
### * Optional after uploading ###
##################################
DOWNLOAD_ORIGINAL_URL: Optional[Union[str, dict]] = {
    "Images": "https://datasets-u2m.s3.eu-west-3.amazonaws.com/tomatOD_images.zip",
    "Bounding box annotations (train and validation sets)": "https://datasets-u2m.s3.eu-west-3.amazonaws.com/tomatOD_annotations.zip",
}
# Optional link for downloading original dataset (e.g. "https://some.com/dataset/download")

CLASS2COLOR: Optional[Dict[str, List[str]]] = {
    "unripe": [126, 211, 33],
    "semi-ripe": [248, 231, 28],
    "fully-ripe": [208, 2, 27],
}
# If specific colors for classes are needed, fill this dict (e.g. {"class1": [255, 0, 0], "class2": [0, 255, 0]})

PAPER: Optional[
    str
] = "https://isprs-archives.copernicus.org/articles/XLIII-B3-2020/1077/2020/isprs-archives-XLIII-B3-2020-1077-2020.pdf"
CITATION_URL: Optional[str] = "https://github.com/up2metric/tomatOD#citations"
ORGANIZATION_NAME: Optional[Union[str, List[str]]] = "up2metric, Greece"
ORGANIZATION_URL: Optional[Union[str, List[str]]] = "http://www.up2metric.com/computer-vision-ai/"
TAGS: List[str] = None

##################################
###### ? Checks. Do not edit #####
##################################


def check_names():
    fields_before_upload = [PROJECT_NAME, PROJECT_NAME_FULL]
    if any([field is None for field in fields_before_upload]):
        raise ValueError("Please fill all fields in settings.py before uploading to instance.")


def get_settings():
    settings = {
        "project_name": PROJECT_NAME,
        "project_name_full": PROJECT_NAME_FULL,
        "license": LICENSE,
        "applications": APPLICATIONS,
        "cv_tasks": CV_TASKS,
        "annotation_types": ANNOTATION_TYPES,
        "release_year": RELEASE_YEAR,
        "homepage_url": HOMEPAGE_URL,
        "preview_image_id": PREVIEW_IMAGE_ID,
        "github_url": GITHUB_URL,
    }
    if any([field is None for field in settings.values()]):
        raise ValueError("Please fill all fields in settings.py after uploading to instance.")

    settings["download_original_url"] = DOWNLOAD_ORIGINAL_URL
    settings["class2color"] = CLASS2COLOR
    settings["paper"] = PAPER
    settings["citation_url"] = CITATION_URL
    settings["organization_name"] = ORGANIZATION_NAME
    settings["organization_url"] = ORGANIZATION_URL
    settings["tags"] = TAGS if TAGS is not None else []

    return settings
