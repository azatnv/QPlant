#!/bin/sh
java -version

uvicorn app:app --port 8502 --host 0.0.0.0