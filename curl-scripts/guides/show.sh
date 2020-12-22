#!/bin/bash

curl "http://localhost:8000/guides/${ID}" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo
