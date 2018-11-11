# Copyright 2016 Google Inc.
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

from .Model import Model
from google.cloud import datastore


def from_datastore(entity):
    """
    Translate Datastore results into the format expected by the application.

    Datastore typically returns:
        [Entity{key: (kind, id), prop: val, ...}]

    This returns:
        [ title, author, ingredients, time, skill, description ]
    where title, author, ingredients, and description are strings, and time and
    skill are integers.
    """
    if not entity:
        return None
    if isinstance(entity, list):
        entity = entity.pop()
    return [
        entity['title'],
        entity['author'],
        entity['ingredients'],
        entity['time'],
        entity['skill'],
        entity['description']
    ]


class model(Model):
    def __init__(self):
        self.client = datastore.Client('plasma-kit-218105')

    def select(self):
        query = self.client.query(kind='Recipe')
        entities = list(map(from_datastore, query.fetch()))
        return entities

    def insert(self, title, author, ingredients, time, skill, description):
        key = self.client.key('Recipe')
        rev = datastore.Entity(key)
        rev.update({
            'title': title,
            'author': author,
            'ingredients': ingredients,
            'time': time,
            'skill': skill,
            'description' : description
        })
        self.client.put(rev)
        return True
