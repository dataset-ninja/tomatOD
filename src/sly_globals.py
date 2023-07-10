import os
import sys
from collections import defaultdict
from pathlib import Path

import supervisely as sly

# my_app = sly.AppService()
# api: sly.Api = my_app.public_api

root_source_dir = str(Path(sys.argv[0]).parents[1])
sly.logger.info(f"Root source directory: {root_source_dir}")
sys.path.append(root_source_dir)

# TASK_ID = int(os.environ["TASK_ID"])
# TEAM_ID = sly.env.team_id()
# WORKSPACE_ID = sly.env.workspace_id()

logger = sly.logger

# train_ds = os.environ["modal.state.train"]
# test_ds = os.environ["modal.state.test"]

datasets = ["Train", "Test"]

# for ds in [train_ds, test_ds]:
#     if len(ds) != 2:
#         datasets.append(ds[1:-1].replace('\'', ''))

# if len(datasets) == 0:
#     logger.warn('You have not selected a dataset to import')
#     my_app.stop()

train_percent = 100
test_percent = 100

sample_img_count = {"Train": round(2.22 * train_percent), "Test": round(0.55 * test_percent)}

# project_name = "TomatoOD"
work_dir = "tomato_data"
images_url = "https://datasets-u2m.s3.eu-west-3.amazonaws.com/tomatOD_images.zip"
annotations_url = "https://datasets-u2m.s3.eu-west-3.amazonaws.com/tomatOD_annotations.zip"

images_arch_name = "tomatOD_images.zip"
annotations_arch_name = "tomatOD_annotations.zip"

anns_folder = "tomatOD_annotations"
ann_prefix = "tomatOD_"
ann_ext = ".json"
batch_size = 30
class_name = "tomato"
train_ds = "Train"

# obj_class = sly.ObjClass(class_name, sly.Rectangle)
# obj_class_collection = sly.ObjClassCollection([obj_class])

obj_class_unripe = sly.ObjClass("unripe", sly.Rectangle)
obj_class_semi_ripe = sly.ObjClass("semi-ripe", sly.Rectangle)
obj_class_fully_ripe = sly.ObjClass("fully-ripe", sly.Rectangle)

cls_to_obj_classes = {
    "unripe": obj_class_unripe,
    "semi-ripe": obj_class_semi_ripe,
    "fully-ripe": obj_class_fully_ripe,
}

# tag_metas = [tag_meta_unripe, tag_meta_semi_ripe, tag_meta_fully_ripe]
# tag_meta_collection = sly.TagMetaCollection(tag_metas)
meta = sly.ProjectMeta(obj_classes=[obj_class_unripe, obj_class_semi_ripe, obj_class_fully_ripe])

# storage_dir = sly.app.get_data_dir()
storage_dir = "./debug_data"
work_dir_path = os.path.join(storage_dir, work_dir)
sly.io.fs.mkdir(work_dir_path)
images_archive_path = os.path.join(work_dir_path, images_arch_name)
annotations_archive_path = os.path.join(work_dir_path, annotations_arch_name)

image_name_to_id = {}
id_to_bbox_anns = defaultdict(list)
id_to_anns = defaultdict(list)
name_to_size = {}
category_id_to_name = {}
