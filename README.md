# pymonero-gui

- Proof-of-concept to develop with monero in Python. Currently only creates & shows a monero wallet (main public address & seed)

- TESTING ONLY. Filename & testnet hardcoded in init app.py

- Uses https://github.com/ehanoc/pymonero (Python C++ bindings)

# Build
- Clone
- ``` git submodule update --init --recursive --remote ```
- build & install python module ``` sh build.sh ``` (Wait, will build monero first)
- run ``` python3 app.py ```
