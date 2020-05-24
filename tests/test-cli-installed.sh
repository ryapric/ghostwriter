#!/usr/bin/env bash

# This script tests the CLI as though it were installed & called locally, to
# avoid mocking it super hard in Python


#########
# SETUP #
#########

python3 -m venv --clear venv-gw
source venv-gw/bin/activate
pip3 install . >/dev/null

cd tests || exit 1

# Set test failures file, make sure it's empty and gitignored
export results=cli-test-failures
rm -rf "${results}" && touch "${results}"
touch .gitignore
if ! grep -q "${results}" .gitignore; then
  echo "${results}" >> .gitignore;
fi

# Set failure file helper function
add-test-failure() {
  printf ">>> %s\n" "$@" >> "${results}"
}


#########
# TESTS #
#########

# Both CLI entrypoints can be reached (expected to be on PATH)
for entrypoint in ghostwrite gw; do
  "${entrypoint}" -h >/dev/null || add-test-failure "Entrypoint '${entrypoint}' not found"
done


############
# FINALIZE #
############
printf "\n=== CLI TEST RESULTS === \n"
if [[ $(wc -l "${results}" | awk '{ print $1 }') -gt 0 ]]; then
  cat "${results}"
  exit 1
else
  printf ">>> All tests passed!\n"
fi
