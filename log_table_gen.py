from mpmath import mp

if __name__ == "__main__":
  input_precision = 3 
  output_precision = 6
  mp.dps = output_precision + 10
  table_raw = []
  number = mp.mpf(1.0)
  while number <= mp.mpf(10.0):
    table_raw.append([number, mp.log10(number)])
    number = number + mp.power(10, -input_precision)
  with mp.workdps(output_precision):
    print "\n".join([str(item[0])+" "+str(item[1]) for item in table_raw])
