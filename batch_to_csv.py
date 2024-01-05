import re

from csv import DictWriter
from pathlib import Path

HEADER = ['Identifier', 'Message Body']

# Create output path if not exists
path = Path('data')
path.mkdir(parents=True, exist_ok=True)
output_path = path

# Open the output CSV for writing
with open(output_path / 'whpool_sagemaker.csv', 'w') as csv_file:
    csv_writer = DictWriter(
        csv_file,
        fieldnames=HEADER,
        extrasaction='ignore',
        escapechar='\\',
        delimiter=',',
    )
    # Add the headers
    csv_writer.writeheader()

    # Iterate over files
    for file in Path('./data/whpool_month_of_2021-04/').rglob('*.html'):
        file_name = Path(file).stem
        print(file_name)

        message_body = open(file).read()
        message_body = message_body.strip()
        message_body = message_body.replace(',', '')

        # Remove tags
        pattern = re.compile('<.*?>')
        message_body = re.sub(pattern, '', message_body)

        # Write CSV row
        csv_writer.writerow(
            {
                'Identifier': file_name,
                'Message Body': message_body,
            }
        )
