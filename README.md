CSV files of UNFCCC emissions data, downloaded from the UNFCCC ["Detailed Data By Party"](http://di.unfccc.int/detailed_data_by_party) interface.

See also the [GHG data from UNFCCC](https://unfccc.int/process-and-meetings/transparency-and-reporting/greenhouse-gas-data/ghg-data-unfccc/ghg-data-from-unfccc)
pages.

[![DOI](https://www.zenodo.org/badge/DOI/10.5281/zenodo.1300334.svg)](https://doi.org/10.5281/zenodo.1300334)

Contributors:

- Robert Gieseke (<rob.g@web.de>)
- Johannes Gütschow (<johannes.guetschow@pik-potsdam.de>)


## Data

The data is available in two files, one for Annex-I and one for Non-Annex-I parties.
Is is in a "wide" format, with base year and individual years as columns.

The current release contains data donwloaded on July 31 2021.

Note also the following footnotes from the data interface:

> Note 1: The reporting and review requirements for GHG inventories are different for Annex I and non-Annex I Parties. The definition format of data for emissions/removals from the forestry sector is different for Annex I and non-Annex I Parties.

> Note 2: Base year data in the data interface relate to the base year under the Climate Change Convention (UNFCCC). The base year under the Convention is defined slightly different than the base year under the Kyoto Protocol. An exception is made for European Union (KP) whereby the base year under the Kyoto Protocol is displayed.

> Note 3: Some non-Annex I Parties submitted their GHG inventory data using the format of the 2006 IPCC Guidelines in reporting GHG emissions/removals. For this reason, these data could not be included in the data interface. However, the data are available in the national communications (Andorra, Antigua and Barbuda, Armenia, Bahrain, Bangladesh, Bhutan, Brazil, Brunei Darussalam, Cabo Verde, Cook Islands, Costa Rica, Côte d'Ivoire, Colombia, Cuba, Equatorial Guinea, Eswatini, Fiji, Gambia, Georgia, Grenada, Ghana, Honduras, Indonesia, Iran, Jamaica, Kuwait, Malaysia, Mauritania, Mauritius, Mexico, Mongolia, Montenegro, Namibia, Nicaragua, Nigeria, Panama, Oman, Republic of Moldova, Rwanda, Samoa, Serbia, Sierra Leone, Singapore, Somalia, South Africa, Suriname, Timor-Leste, United Arab Emirates, Vanuatu, Venezuela, Viet Nam, and Zambia) and biennial update reports (Afghanistan, Andorra, Antigua and Barbuda, Argentina, Armenia, Azerbaijan, Belize, Benin, Cambodia, Chile, Colombia, Costa Rica, Côte d'Ivoire, Dominican Republic, Egypt, El Salvador, Ghana, Georgia, Guinea-Bissau, Honduras, India, Indonesia, Jordan, Laos Peoples Republic, Malaysia, Mauritania, Mexico, Mongolia, Montenegro, Morocco, Namibia, Nigeria, North Macedonia, Oman, Panama, Paraguay, Papua New Guinea, Peru, Republic of Moldova, Serbia, Singapore, South Africa, Tajikistan, Thailand, Togo, Tunisia, Uruguay, Uganda, Viet Nam, and Zambia).

> Note 5: Data displayed on the data interface are "as received" from Parties. The publication of Party submissions on this website does not imply the expression of any opinion whatsoever on the part of the UNFCCC or the Secretariat of the United Nations concerning the legal status of any country, territory, city or area or of its authorities, or concerning the delimitation of its frontiers or boundaries as may be referred to in any of the submissions.


## Processing

To update the dataset once newer data becomes available, the following steps need to be run. It might be necessary to adjust the scripts if the data format or website changes. Python3 and Make are required. The scripts should run on Linux or macOS.

Run

```shell
make mappings
```

to download category and group mappings,

```shell
make download
```

to download the data as JSON files and

```shell
make process
```

to generate CSV files for Annex-I and Non-Annex-I.

To remove all downloaded and generated files run

```shell
make clean
```

This needs to be done to check for updated data. To continue an interrupted
download or check for new data simply re-run `make download`.
Files already downloaded are skipped.


## License

The [UNFCCC website](http://unfccc.int/home/items/2783.php) states:

> All official texts, data and documents are in the public domain and may be freely downloaded, copied and printed provided no change to the content is introduced, and the source is acknowledged.
