from Parser import Parser
from XLSXExporter import XLSXExporter

input_filename = 'dados'
output_filename = 'output.xlsx'

if __name__ == '__main__':
    with open(input_filename, 'r') as file:
        xlsExporter = XLSXExporter(output_filename)
        data = file.read()
        parsed_data = Parser.parse(data)
        for lfc_id in parsed_data:
            xlsExporter.export(lfc_id, "Timestamp; State; TempA; TempB\n" + parsed_data[lfc_id])
        xlsExporter.save()