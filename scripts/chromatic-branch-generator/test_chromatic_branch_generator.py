# Assuming your module is named `chromatic_url_generator.py`
from chromatic_branch_generator import generate_chromatic_url


def test_valid_branch_name():
    url = generate_chromatic_url("feature-branch", "app123")
    assert url == "https://feature-branch--app123.chromatic.com"


def test_valid_commit_hash():
    url = generate_chromatic_url("abcdef1234567890", "app123")
    assert url == "https://abcdef1234567890--app123.chromatic.com"


def test_replace_invalid_characters():
    url = generate_chromatic_url("feature/branch@2023", "app123")
    assert url == "https://feature-branch-2023--app123.chromatic.com"


def test_truncate_long_branch_name():
    branch_name = "release/v1.2.3/DEV-22335-feature-branch"
    # expected =
    url = generate_chromatic_url(branch_name, "app123")
    expected = 'https://release-v1-2-3-DEV-22335-feature-bran--app123.chromatic.com'
    assert url == expected


def test_already_valid_branch_name():
    url = generate_chromatic_url("this-is-valid-123", "app123")
    assert url == "https://this-is-valid-123--app123.chromatic.com"
