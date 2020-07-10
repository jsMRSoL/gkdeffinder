#!/usr/bin/python3
import re

LEMMATA = "Perseus_Data/greek-lemmata.txt"


def get_headword(input):

    pat_str = r'[^a-z()\/\=-]h[()\/\=]{,2}dh[()\/\=]{,2}\b.*?\)\s'
    pattern = re.compile(pat_str)

    # extractor_pattern = re.compile(r'^([\S]*?).*?(' + pat_str + r') ([^)].*\))[\t]{,2}')

    with open(LEMMATA, 'r') as f:
        for line in f.readlines():
            matches = pattern.finditer(line)
            match_count = 0
            for match in matches:
                match_count += 1
                headword = line.split()[0]
                print(f'Headword: {headword}')
                print(f'{match_count}: {match.group(0).strip()}')
                if match_count == 10:
                    return


get_headword("hdh")
