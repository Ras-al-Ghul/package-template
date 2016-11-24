Data directory
==============

This directory contains data files included with the affiliated package source
code distribution. Note that this is intended only for relatively small files
- large files should be externally hosted and downloaded as needed.

Data which is to be used in multiple tests around the codebase can be put in
`test` and the filepath obtained witht the `{{ cookiecutter.module_name
}}.data.test.get_test_filename` function.

