import os
import re
import json
import file_processing.file_paths as demo_paths

with open(demo_paths.SETTINGS_PATH, 'r') as file:
    settings = json.load(file)

ACCESS_PATH = settings["Access Database Path"]
RAW_DATA_PATH = settings["Raw Data Path"]
RAW_DATA_SHEET = settings["Raw Data Sheet Name"]
ACCESS_TBL = settings["Import Access Table Name"]
ACCESS_FORM = settings["Access Form Name"]
SF_UPLOAD = settings["SF Upload File Name"]
SF_EXCLUDE = settings["SF Exclude File Name"]
UDB_UPLOAD = settings["UDB Upload File Name"]
UDB_EXCLUDE = settings["UDB Exclude File Name"]
DEMO_DEST_PATH = settings["Demo Folder Destination Path"]
SOP_PATH = settings["Demo SOP Path"]
