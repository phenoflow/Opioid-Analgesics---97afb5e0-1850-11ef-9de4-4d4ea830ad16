# Matthew J Carr, Darren M Ashcroft, Evangelos Kontopantelis, David While, Yvonne Awenat, Jayne Cooper, Carolyn Chew-Graham, Nav Kapur, Roger T Webb, 2024.

import sys, csv, re

codes = [{"code":"73078020","system":"multilex"},{"code":"4551020","system":"multilex"},{"code":"4549020","system":"multilex"},{"code":"87620020","system":"multilex"},{"code":"97288020","system":"multilex"},{"code":"73071020","system":"multilex"},{"code":"73145020","system":"multilex"},{"code":"62391020","system":"multilex"},{"code":"96516020","system":"multilex"},{"code":"65617020","system":"multilex"},{"code":"99815020","system":"multilex"},{"code":"73131020","system":"multilex"},{"code":"97487020","system":"multilex"},{"code":"10627020","system":"multilex"},{"code":"42244020","system":"multilex"},{"code":"64812020","system":"multilex"},{"code":"87618020","system":"multilex"},{"code":"65620020","system":"multilex"},{"code":"80388020","system":"multilex"},{"code":"64465020","system":"multilex"},{"code":"80382020","system":"multilex"},{"code":"99803020","system":"multilex"},{"code":"50530020","system":"multilex"},{"code":"76930020","system":"multilex"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('opioid-analgesics-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["opioid-analgesics-375mg---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["opioid-analgesics-375mg---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["opioid-analgesics-375mg---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
