#!/bin/bash

# Downloads groups, categories, year, etc. mappings from the respective API
# endpoints.

# var apiEndpoints = {
#   parties: { url: 'parties', autoLoad: true },
#   yearGroups: { url: 'years/groups', autoLoad: true },
#   categories: { url: 'dimension-instances/category', autoLoad: true },
#   gases: { url: 'dimension-instances/gas', autoLoad: true },
#   units: { url: 'conversion', autoLoad: true },
#   records: { url: 'records/detail-by-category', autoLoad: false }
# };

cd `dirname $0`/api-mappings
wget http://di.unfccc.int/api/parties -q -O- | \
  python3 -m json.tool > parties.json
wget http://di.unfccc.int/api/years/groups -q -O- | \
  python3 -m json.tool > years.json
wget http://di.unfccc.int/api/dimension-instances/category -q -O- | \
  python3 -m json.tool > categories.json
wget http://di.unfccc.int/api/dimension-instances/gas -q -O- | \
  python3 -m json.tool >  gases.json
wget http://di.unfccc.int/api/conversion -q -O- | \
  python3 -m json.tool > conversion.json
pwd
ls -l
