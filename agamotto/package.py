# Copyright 2014 Numenta
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


from agamotto.utils import execute


def installed(packageName):
  """Confirm that a package is installed"""
  # TODO: Make this work with apt/dpkg
  try:
    return (int(execute("yum list installed %s | grep -c %s" % (packageName, packageName))) > 0)
  except Exception, e:
    return False


def is_installed(packageName):
  """Convenience alias to make the tests look nicer"""
  return installed(packageName)
