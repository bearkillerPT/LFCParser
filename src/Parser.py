import re

class Parser:
    @staticmethod
    def parse(data):
        res = {}
        lines = data.split('\n')
        for i in range(len(lines)):
            if lines[i].strip() == '' or Parser.classifyEntry(lines[i]) == "tempertature_data":
                continue
            line_split = lines[i].split(',')
            timestamp = line_split[0][1:-1]
            lines[i] = Parser.cleanLine(line_split[1])
            if Parser.classifyEntry(lines[i]) == "lfc_state":
                lines[i+1] = Parser.cleanLine(lines[i+1].split(',')[1])
                if Parser.classifyEntry(lines[i+1]) == "tempertature_data":
                    lfc_id, state = Parser.extractLFCSate(lines[i])
                    tempA, tempB = Parser.extractTemperatureData(lines[i+1])
                    if lfc_id not in res:
                        res[lfc_id] = ""
                    res[lfc_id] += f"{timestamp}; {state}; {tempA}; {tempB}\n"
                    i += 1
        return res
    @staticmethod  
    def extractLFCSate(line):
        if line.startswith('*01 Po;'):
            return line.split(';')[1], line.split(';')[3]
        elif 'Hh*01 Ns;' in line:
            # (prefix)Hh*01 Ns;02;TempReadOk;RxT(ms);43;SttV;20; 
            # get the 02 and 20
            lfc_pattern = r'01 Ns;(\d+);'
            sttV_pattern = r'SttV;(\d+);'
            return re.search(lfc_pattern, line).group(1), re.search(sttV_pattern, line).group(1)
    
    @staticmethod  
    def extractTemperatureData(line):
        if line.startswith('*01 rA;01;'):
            return line.split(';')[3].replace('.', ','), line.split(';')[5].replace('.', ',')
        elif line.startswith('*01 Nx;'):
            return line.split(';')[3].replace('.', ','), line.split(';')[5].replace('.', ',')
    
    @staticmethod
    def classifyEntry(entry):
        if entry.startswith('*01 rA;01;') or entry.startswith('*01 Nx;'):
            return "tempertature_data"
        elif entry.startswith('*01 Po;') or 'Hh*01 Ns;' in entry:
            return 'lfc_state'
    @staticmethod
    def cleanLine(line):
        return line


if __name__ == '__main__':
    with open('dados', 'r') as file:
        data = file.read()
        print(Parser.parse(data))