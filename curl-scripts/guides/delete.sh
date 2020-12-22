#!/bin/bash

curl "http://localhost:8000/guides/${ID}" \
  --include \
  --request DELETE \
  --header "Authorization: Token ${TOKEN}"

echo
