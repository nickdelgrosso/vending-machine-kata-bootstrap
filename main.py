import pytest


def get_the_answer():
  return 10


def test_the_answer():
  assert get_the_answer() == 42
