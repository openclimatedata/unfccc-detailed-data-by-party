import os

import requests

from mappings import categories, gases, parties, years

path = os.path.dirname(os.path.realpath(__file__))
outpath = {
    "annexOne": os.path.join(path, "../archive/annex-one"),
    "nonAnnexOne": os.path.join(path, "../archive/non-annex-one")
}

url = "http://di.unfccc.int/api/records/detail-by-category"


def get_children(items, parent=None):
    all_categories = []
    for item in items:
        if parent:
            item["parent"] = parent
        else:
            item["parent"] = item["name"]
        if "children" in item and item["children"] is not None:
            all_categories.append(item)
            all_categories = (
                all_categories + get_children(item["children"], item["name"]))
        else:
            all_categories.append(item)
    return all_categories

for group in ["annexOne", "nonAnnexOne"]:
    all_categories = get_children(categories[group])
    for category in all_categories:
        parent_category = category["parent"].replace("  ", " ").replace(
            "/", "_-_")
        name_category = category["name"].replace("  ", " ").replace(
            "/", "_-_")
        for gas in gases[group]:
            name_gas = gas["name"]
            params = {
                "partyIds": parties[group].values(),
                "yearIds": years[group],
                "categoryId": category["id"],
                "gasId": gas["id"]
            }
            filename = (parent_category + "___" + name_category +
                        "___" + name_gas + ".json")
            fullpath = os.path.join(outpath[group], filename)
            if os.path.exists(fullpath):
                print("Skipping (already exists): archive/{}: {}".format(
                    group, filename))
                continue
            print("archive :: {} :: {}".format(group, filename))
            r = requests.get(url, params=params)
            if r.ok:
                with open(fullpath, "w") as f:
                    f.write(r.text)
