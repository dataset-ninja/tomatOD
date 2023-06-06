import os

from dotenv import load_dotenv

import supervisely as sly

if sly.is_development():
    load_dotenv(os.path.expanduser("~/ninja.env"))
    load_dotenv("local.env")


from dataset_tools.convert.tomatod.main import to_supervisely

WORKSPACE_ID = sly.env.workspace_id()

api = sly.Api.from_env()
project_id = to_supervisely(api, WORKSPACE_ID)

print("Project id is", project_id)
