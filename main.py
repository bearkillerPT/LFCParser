from Parser import Parser
from XLSXExporter import XLSXExporter

input_filename = 'dados'
output_filename = 'output.xlsx'

if __name__ == '__main__':
    with open(input_filename, 'r') as file:
        xlsExporter = XLSXExporter(output_filename)
        data = file.read()
        parsed_data = Parser.parse(data)
        ordered_keys = sorted(parsed_data.keys())
        for lfc_id in ordered_keys:
            xlsExporter.export(lfc_id, "Timestamp; State; TempA; TempB\n" + parsed_data[lfc_id])
        xlsExporter.save()