#!/usr/bin/env bash

# remove obsolete files, because are not cleaned during generations
rm -rf /api/*

# generate pydantic classes from swagger
poetry run datamodel-codegen \
  --disable-timestamp \
  --enable-version-header \
  --use-schema-description \
  --use-field-description \
  --allow-population-by-field-name \
  --use-standard-collections \
  --reuse-model \
  --openapi-scopes paths \
  --input /swagger/uniconfigV3.yaml \
  --output /api/ \
  --target-python-version 3.10

# use default formatting
poetry run ruff --fix . || true
