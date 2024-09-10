#!/bin/bash

rasa run --cors "*" &
rasa run actions &
python -m http.server 8080


