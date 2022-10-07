#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 18:55:19 2019

@author: krishnaparekh
"""

import csv
from faker import Faker
import datetime

def datagenerate(records, headers):
    with open("People_data.csv", 'wt') as csvFile:
        writer = csv.DictWriter(csvFile, fieldnames=headers)
        writer.writeheader()
        for i in range(records):
            writer.writerow({
                    "Prefix" : f"test {i}",
                    })
    
if __name__ == '__main__':
    records = 2000000
    headers = ["Prefix",]
    datagenerate(records, headers)
    print("CSV generation complete!")