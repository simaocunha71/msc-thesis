sudo apt  install cargo
export PATH="$HOME/.cargo/bin:$PATH"
cargo install weggli --rev=9d97d462854a9b682874b259f70cc5a97a70f2cc --git=https://github.com/weggli-rs/weggli
export WEGGLI_PATH=weggli

pip3 install -r CybersecurityBenchmarks/requirements.txt