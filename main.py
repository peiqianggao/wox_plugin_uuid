#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @CreateDate             : 4/11/2017 11:51 AM
# @Author                 : gaopq (peiqianggao@gmail.com)
# @Version                : 001
# @File                   : main.py
# @ModifyDate             :
# @Descriptions           :
# @ChangeLog              :


import os
import uuid
import copy
import collections
from wox import Wox

result_template = {
    'Title': '{}',
    'SubTitle': 'Copy to clipboard',
    'IcoPath': 'Images/uuid.jpg',
    'JsonRPCAction': {
        'method': 'copyToClipboard',
        'parameters': ['{}'],
    }
}


class Main(Wox):
    def query(self, key=None):
        results = list()
        u1 = uuid.uuid1().hex.strip()
        u3 = uuid.uuid3(uuid.NAMESPACE_DNS, key).hex.strip()
        u5 = uuid.uuid5(uuid.NAMESPACE_DNS, key).hex.strip()
        uuids = collections.OrderedDict(
        # uuids = dict(
            uuid1 = u1,
            uuid1_upper = u1.upper(),
            uuid3 = u3,
            uuid3_upper = u3.upper(),
            uuid5 = u5,
            uuid5_upper = u5.upper()
        )

        for key, u in uuids.items():
            res = copy.deepcopy(result_template)
            res['Title'] = res['Title'].format('{}: {}'.format(key, u))
            res['JsonRPCAction']['parameters'][0] = res['JsonRPCAction']['parameters'][0].format(u)
            results.append(res)
            res = None

        return results

    def copyToClipboard(self, value):
        command = 'echo ' + value.strip() + '| clip'
        os.system(command)

if __name__ == '__main__':
    Main()
