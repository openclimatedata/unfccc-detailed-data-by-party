import json
import os

_path = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    "api-mappings"
)

# Party Ids
party_groups = json.load(open(os.path.join(_path, "parties.json")))

parties = {}
no_data = []
# Annex I
parties["annexOne"] = {}
assert(party_groups[1]["name"] == "Annex I")
for party in party_groups[1]["parties"]:
    parties["annexOne"][party["name"]] = party["id"]
    if "noData" in party and party["noData"] == True:
        no_data.append(party["name"])

# Non Annex I
parties["nonAnnexOne"] = {}
assert(party_groups[2]["name"] == "Non Annex I")
for party in party_groups[2]["parties"]:
    parties["nonAnnexOne"][party["name"]] = party["id"]
    if "noData" in party and party["noData"] == True:
        no_data.append(party["name"])


# Year Ids, see years.json
# zero is base year; 1990 is 32
years = {}
years["annexOne"] = [0] + list(range(32, 59))
years["nonAnnexOne"] = list(range(32, 59))

# Category Ids
categories = json.load(open(os.path.join(_path, "categories.json")))

# Gas Ids
gases = json.load(open(os.path.join(_path, "gases.json")))

# Conversion
_units = json.load(open(os.path.join(_path, "conversion.json")))["units"]
units = {item["id"]: item["name"] for item in _units}
