import csv
def process_csv(file_path):
with open(file_path, 'r') as csvfile:
reader = csv.reader(csvfile)
next(reader, None)
for row in reader:
lcn, lsn_l, lsn_h, freq_mhz = map(float, row)
freq_hz = int(freq_mhz * 1e6)
print(f' <timeslot downlink="{freq_hz}" uplink="0" lsn="{int(lsn_l)}"/>')
print(f' <timeslot downlink="{freq_hz}" uplink="0" lsn="{int(lsn_h)}"/>')
if __name__ == "__main__":
csv_file_path = "orion.csv"
process_csv(csv_file_path)
