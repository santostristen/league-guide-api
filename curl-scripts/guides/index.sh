#!/bin/bash

curl "http://localhost:8000/guides" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo
