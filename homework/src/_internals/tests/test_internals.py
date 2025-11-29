### Test Internals

import sys

from ...wordcount import parse_args
from ..read_all_lines import read_all_lines


def test_parse_args():
    """Llamada en el prompt:
    $ python3 -m homework data/input/ data/output/
    """
    test_args = ["homework", "data/input/", "data/output/"]
    sys.argv = test_args

    input_folder, output_folder = parse_args()

    assert input_folder == test_args[1]
    assert output_folder == test_args[2]


def test_read_all_lines():
    input_folder = "data/input/"
    lines = read_all_lines(input_folder)
    assert len(lines) > 0
    assert any(
        "Analytics refers to the systematic computational analysis of data" in line
        for line in lines
    )


# import subprocess

# python3 -m homework data/input data/output
# from ...wordcount import parse_args


# def test_parse_args():

#    result = subprocess.run(
#        ["python", "-m", "homework", "data/input/", "data/output/"],
#        capture_output=True,
#        text=True,
#    )

#    assert result.returncode == 0
#    assert "input: data/input/" in result.stdout
#    assert "output: data/output/" in result.stdout
