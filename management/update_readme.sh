#!/bin/bash
echo "Create or update README.MD"
touch ../README.MD
echo "Header"
echo "# List of certificates" > ../README.MD
echo "Date of update"
echo "## Updated: $(date +'%Y-%m-%d')" >> ../README.MD
echo "Get list of certificates"
echo $(python3 list_all.py) >> ../README.MD
