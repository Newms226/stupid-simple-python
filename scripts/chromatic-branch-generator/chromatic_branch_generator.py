import re
import os
import argparse


def generate_chromatic_url(input_string, app_id):
    """
    Generates a Chromatic URL by replacing any character that is not a letter, digit,
    or dash with a dash, and truncating if necessary.

    See https://www.chromatic.com/docs/permalinks/#build-your-own-permalink
    """
    # Detect if input is a commit hash (7 to 40 hexadecimal characters)
    if re.match(r'^[0-9a-fA-F]{7,40}$', input_string):
        url = f"https://{input_string}--{app_id}.chromatic.com"
    else:
        # Replace any character that is not a letter, digit, or dash with a dash
        sanitized_branch = re.sub(r'[^a-zA-Z0-9-]+', '-', input_string)
        # Truncate to 37 characters if longer
        if len(sanitized_branch) > 37:
            sanitized_branch = sanitized_branch[:37]
        url = f"https://{sanitized_branch}--{app_id}.chromatic.com"

    return url


def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Generate Chromatic URLs.")
    parser.add_argument("input_string", help="Branch name or commit hash")
    args = parser.parse_args()

    # Read the Chromatic App ID from environment variable
    app_id = os.getenv('NINETY_CHROMATIC_ID')
    if not app_id:
        print("Error: NINETY_CHROMATIC_ID environment variable is not set.")
        return

    # Generate and print the Chromatic URL
    url = generate_chromatic_url(args.input_string, app_id)
    print("Chromatic URL:", url)


if __name__ == "__main__":
    main()
