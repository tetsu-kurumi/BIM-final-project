"""
To get the joystick data from the demonstration, while running shutter demonstration, run "rostopic echo /joy > {filename}"
Command line arg when running this file should be python3 rosbag_to_csv {filename} {output_filename.csv}
"""


import csv
import yaml
import sys

def convert_to_csv(yaml_text_file, output_csv):
    # Parse the YAML text
    with open (yaml_text_file, 'r') as yaml_text:
        data_list = list(yaml.safe_load_all(yaml_text))

        # Write to CSV file
        with open(output_csv, mode='w', newline='') as csv_file:
            fieldnames = ['seq', 'secs', 'axes']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            # Write header
            writer.writeheader()

            # Write data
            for data in data_list:
                if data is not None:
                    seq = data['header']['seq']
                    secs = data['header']['stamp']['secs']
                    axes = data['axes']

                    writer.writerow({'seq': seq, 'secs': secs, 'axes': axes})


if __name__ == "__main__":
    yaml_text_file  = sys.argv[1]
    output_csv = sys.argv[2]
    convert_to_csv(yaml_text_file, output_csv)
    print(f"Conversion completed. Data written to {output_csv}")
