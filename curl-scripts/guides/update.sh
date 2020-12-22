#!/bin/bash

curl "http://localhost:8000/guides/${ID}" \
  --include \
  --request PATCH \
  --header "Content-Type: application/json" \
  --header "Authorization: Token ${TOKEN}" \
  --data '{
    "guide": {
      "title": "'"${TEXT}"'",
      "text": "'"${TEXT}"'"
    }
  }'

echo
