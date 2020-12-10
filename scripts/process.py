#!/usr/env/bin python3

import glob
import json
import os

import pandas as pd

from mappings import units, no_data


path = os.path.dirname(os.path.realpath(__file__))
archivepath = os.path.join(path, "../archive")
datapath = os.path.join(path, "../data")


metadata = ["Party", "Category", "Gas", "Unit"]
csv_paths = {
    "annex-one": os.path.join(datapath, "detailed-data-by-country-annex-one.csv"),
    "non-annex-one": os.path.join(
        datapath, "detailed-data-by-country-non-annex-one.csv"
    ),
}

for group in ["annex-one", "non-annex-one"]:
    files = glob.glob(os.path.join(archivepath, group, "*.json"))
    data = []
    print(group, len(files), " JSON files")
    for filename in files:
        basename = os.path.splitext(os.path.basename(filename))[0]
        print(group, basename)
        parent_category, _, gas = basename.split("___")
        table = json.load(open(filename))
        index = {i["id"]: i["name"] for i in table["columns"]}

        # Skip empty category/gas combinations.
        if len(table["columns"]) > 0:
            # Shorten e.g. "Last Inventory Year (2016)" to just the year
            index_keys = list(index.keys())
            index[index_keys[-1]] = index[index_keys[-1]][-5:-1]

            parties = table["data"]
            for party in parties:
                name = party["name"]
                rows = party["rows"]
                for row in rows:

                    values = {}
                    values["Party"] = name
                    values["Parent Category"] = parent_category.replace("_-_", "/")
                    values["Category"] = (
                        row["name"].replace("  ", " ").replace("_-_", "/")
                    )
                    values["Gas"] = gas
                    if row["unitId"] is not None:
                        unit = units[row["unitId"]]
                    else:
                        unit = None

                    values["Unit"] = unit
                    for cell in row["cells"]:
                        if "numberValue" in cell:
                            values[index[cell["column"]]] = cell["numberValue"]
                        else:
                            values[index[cell["column"]]] = None

                    data.append(values)

    df = pd.DataFrame(data)

    filtered = df.set_index(["Party", "Parent Category", "Category", "Gas", "Unit"])
    filtered = filtered.dropna(how="all").reset_index()
    filtered = (
        filtered.drop_duplicates()
        .set_index(["Party", "Parent Category", "Category", "Gas", "Unit"])
        .sort_index()
    )

    

    filtered = filtered.reset_index()
    if "Base year" in filtered.columns:  # Annex-One
        meta = [
            "Party",
            "Parent Category",
            "Category",
            "Gas",
            "Unit",
            "Base year",
            ]
    else:
        meta = [
            "Party",
            "Parent Category",
            "Category",
            "Gas",
            "Unit",
        ]    
    
    year_cols = list(set(filtered.columns) - set(meta))
    year_cols.sort()
    ordered = meta + year_cols

 
    filtered = filtered[ordered]

    print("=> ", csv_paths[group])
    party_names = filtered["Party"].unique()

    # Check if countries with no data (listed with attribute "noData" set
    # to 'true' in `parties.json`) have no data.
    assert set(party_names).isdisjoint(set(no_data))

    filtered.to_csv(csv_paths[group], index=False, float_format = '%g')
