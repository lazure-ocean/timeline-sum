#!/bin/bash

# Download datasets
rm -rf datasets
mkdir datasets
cd datasets
wget -i ./timeline_sum/datasets.txt
for F in *.tar.gz; do
    tar -xzvf "$F"
    rm -f "$F"
done
cd ../
