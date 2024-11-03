# dataset API
import os
import pandas as pd
from IPython.display import display,HTML
from PIL import Image


def empty_pants():
    """
    returns empty data frame for pants
    """
    parameters = ["clothing", "top_bot", "color", "length", "style"]
    df = pd.DataFrame(columns=parameters)
    return df

def directory_file(directory):
    """
    creates list of file directories in specified directory
    """
    # gets all files in directory
    pants = os.listdir(directory)
    img_files = []

    # appends all directories into image files
    for filename in pants:
        img_files.append(os.path.join(directory, filename))

    return img_files


def tagging(clothing, top_bot, color, length, style):
    """
    tags clothing image file with specified parameters
    """
    formatted = {'clothing': clothing,
                 'top_bot': top_bot,
                 'color': color,
                 'length': length,
                 'style': style}

    return formatted

def add_data(formatted, df):
    """
    adds data to dataframe
    """
    df = df._append(formatted, ignore_index=True)
    return df


def pants_tagging():
    """
    manual tagging for pants
    """
    pants_directory = 'clothing v.2/pants'
    pants = directory_file(pants_directory)

    # MANUAL TAGGING STARTS FROM HERE IN FILE ORDER. DON'T CHANGE FILE ORDER OR TAGGING GETS DISORGANIZED

    formatted = tagging(pants[0], "bottom", "black", "shorts", "sweats")
    formatted2 = tagging(pants[1], "bottom", "green", "long", "cargo")
    formatted3 = tagging(pants[2], "bottom", "black", "long", "sweats")
    formatted4 = tagging(pants[3], "bottom", "white", "long", "sweats")
    formatted5 = tagging(pants[4], "bottom", "navy", "long", "jeans")
    formatted6 = tagging(pants[5], "bottom", "light blue", "long", "jeans")
    formatted7 = tagging(pants[6], "bottom", "black", "long", "jeans")

    # CONTINUE FROM HERE....

    formats = [formatted, formatted2, formatted3, formatted4,
               formatted5, formatted6, formatted7]

    return formats

def main():
    shirt_directory = 'clothing v.2/shirt'

    # creates empty dataframe
    df = empty_pants()

    formats = pants_tagging()
    # adds data
    for format in formats:
      df = add_data(format, df)
    print(df)

main()