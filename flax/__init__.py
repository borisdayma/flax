# Copyright 2022 The Flax Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


"""Flax API."""

from . import core
from . import io
from . import jax_utils
from . import linen
from . import serialization
from . import traverse_util

# DO NOT REMOVE - Marker for internal deprecated API.
# DO NOT REMOVE - Marker for internal logging.
from .version import __version__
