from Parser import Parser
from XLSXExporter import XLSXExporter
import os

input_files = os.listdir('inputs')

def transform_filename(filename):
    return "outputs/" + filename.replace('.txt', '.xlsx')

if __name__ == '__main__':
    for input_filename in input_files:
        with open("inputs/" + input_filename, 'r') as file:
            xlsExporter = XLSXExporter(transform_filename(input_filename))
            data = file.read()
            parsed_data = Parser.parse(data)
            ordered_keys = sorted(parsed_data.keys())
            for lfc_id in ordered_keys:
                xlsExporter.export(lfc_id, "Timestamp; State; TempA; TempB\n" + parsed_data[lfc_id])
            xlsExporter.save()