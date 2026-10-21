#!/bin/bash
# Double-click to preview the site at http://localhost:8000
cd "$(dirname "$0")"
( sleep 1; open "http://localhost:8000/" ) &
echo "Serving the Capuchin Family Kitchen site at http://localhost:8000 — press Ctrl+C to stop."
python3 -m http.server 8000
