# (C) Datadog, Inc. 2021-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)

# This file is autogenerated.
# To change this file you should edit assets/configuration/spec.yaml and then run the following commands:
#     ddev -x validate config -s <INTEGRATION_NAME>
#     ddev -x validate models -s <INTEGRATION_NAME>



def shared():
    return {'deprecated': {'Release': '8.0.0', 'Migration': 'do this\nand that\n'}}


def instance():
    return {'deprecated': {'Release': '9.0.0', 'Migration': 'do this\nand that\n'}}
