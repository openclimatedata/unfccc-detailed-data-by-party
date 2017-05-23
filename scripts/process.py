#!/usr/env/bin python3

import glob
import json
import os

import pandas as pd

from mappings import *


path = os.path.dirname(os.path.realpath(__file__))
archivepath = os.path.join(path, "../archive")
datapath = os.path.join(path, "../data")


metadata = ["Party", "Category", "Gas", "Unit"]
csv_paths = {
    "annex-one": os.path.join(
        datapath, "detailed-data-by-country-annex-one.csv"),
    "non-annex-one": os.path.join(
        datapath, "detailed-data-by-country-non-annex-one.csv")
}
df_columns = {
    "annex-one": ['Party', 'Parent Category', 'Category', 'Gas', 'Unit',
                  'Base year', '1990', '1991', '1992', '1993', '1994', '1995',
                  '1996', '1997', '1998', '1999', '2000', '2001', '2002',
                  '2003', '2004', '2005', '2006', '2007', '2008', '2009',
                  '2010', '2011', '2012', '2013', '2014', '2015'],
    "non-annex-one": ['Party', 'Parent Category', 'Category', 'Gas', 'Unit',
                      '1990', '1991', '1992', '1993', '1994', '1995', '1996',
                      '1997', '1998', '1999', '2000', '2001', '2002', '2003',
                      '2004', '2005', '2006', '2007', '2008', '2009', '2010',
                      '2011', '2012', '2013']
}

for group in ["annex-one", "non-annex-one"]:

    files = glob.glob(
        os.path.join(archivepath, group, "*.json")
    )
    data = []
    print(group, len(files), " JSON files")
    for filename in files:
        basename = os.path.splitext(os.path.basename(filename))[0]
        parent_category, _, gas = basename.split("___")
        table = json.load(open(filename))
        index = {i["id"]: i["name"] for i in table["columns"]}

        # Shorten e.g. "Last Inventory Year (2015)" to just the year
        index_keys = list(index.keys())
        index[index_keys[-1]] = index[index_keys[-1]][-5:-1]

        parties = table["data"]
        for party in parties:
            name = party["name"]
            rows = party["rows"]
            for row in rows:

                values = {}
                values["Party"] = name
                values["Parent Category"] = parent_category
                values["Category"] = row["name"].replace("  ", " ")
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
    df = df[df_columns[group]]
    filtered = df.set_index(
        ["Party", "Parent Category", "Category", "Gas", "Unit"])
    filtered = filtered.dropna(how="all").reset_index()
    filtered = filtered.drop_duplicates().set_index(
        ["Party", "Parent Category", "Category", "Gas", "Unit"]).sort_index()
    print("=> ", csv_paths[group])
    filtered.to_csv(csv_paths[group])

