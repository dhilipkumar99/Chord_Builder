import argparse
import os

import matplotlib.pyplot as plt
from roifile import ImagejRoi


def main(args):
    roi_file = args.roi_file
    for file in os.listdir(roi_file):
        file_path = os.path.join(roi_file, file)
        if ".png" in file:
            # TODO: Plot image as canvas and accumulate roi polygons, then plot them all at once
            continue
        roi = ImagejRoi.fromfile(file_path)
        roi.plot()


if __name__ == "__main__":
    # Create the parser
    parser = argparse.ArgumentParser(description="Process some data.")

    # Add arguments
    parser.add_argument("--roi_file", required=True, type=str)

    # Parse arguments
    args = parser.parse_args()

    # Call the main function with the parsed arguments
    main(args)
