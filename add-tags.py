from pyzotero import zotero
import os

library_id = "10871458"
library_type = "user"
api_key = "3xsCYj2Pi7oYdseh3B9ssnsf"
collection_id = str(input("collection ID from URL: "))
tag = str(input("tag to add to items: "))

zot = zotero.Zotero(library_id=library_id,library_type=library_type,api_key=api_key)
items = zot.collection_items_top(collection_id)
i=100
while len(zot.collection_items_top(collection_id,start=i))==100: #bypass the pyzotero API limit of 100 items
    items = items+zot.collection_items_top(collection_id,start=i)
print(len(items))

for item in items:
    z = zot.add_tags(item,tag)
    print(z)