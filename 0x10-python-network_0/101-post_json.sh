#!/bin/bash
# Send JSON post request
curl -s -H "Content-Type: application/json" -d @"$2" "$1"
