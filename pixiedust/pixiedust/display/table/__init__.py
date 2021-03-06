# -------------------------------------------------------------------------------
# Copyright IBM Corp. 2016
# 
# Licensed under the Apache License, Version 2.0 (the 'License');
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
# http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an 'AS IS' BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# -------------------------------------------------------------------------------

from .display import TableDisplay
from ..display import *

class TableDisplayMeta(DisplayHandlerMeta):
    @addId
    def getMenuInfo(self,entity):
        clazz = entity.__class__.__name__
        if clazz == "DataFrame":
            return [
                {"categoryId": "Table", "title": "DataFrame Table", "icon": "fa-table", "id": "dataframe"}
            ]
        elif clazz == "GraphFrame":
            return [
                {"categoryId": "Table", "title": "Graph Vertices", "icon": "fa-location-arrow", "id":"vertices"},
                {"categoryId": "Table", "title": "Graph Edges", "icon": "fa-link", "id":"edges"}
            ]
        else:
            return []
    def newDisplayHandler(self,entity):
        return TableDisplay(entity)

registerDisplayHandler(TableDisplayMeta(), isDefault=True)