"""
    Copyright(c) 2021 the original author or authors

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        https: // www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
    or implied. See the License for the specific language governing
    permissions and limitations under the License.
 """

import os
from pydotenv import load_dotenv
from compreface.config.api_list import DETECTION_API

load_dotenv()


DOMAIN: str = os.getenv('DOMAIN')
PORT: str = os.getenv('PORT')
RECOGNIZE_API_KEY: str = os.getenv('RECOGNITION_API_KEY')
DETECTION_API_KEY: str = os.getenv('DETECTION_API_KEY')
VERIFICATION_API_KEY: str = os.getenv('VERIFICATION_API_KEY')
FILE_PATH: str = "tests/common/jonathan-petit-unsplash.jpg"
IMAGE_ID: str = "image-id"
