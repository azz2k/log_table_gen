from mpmath import mp
from jinja2 import Environment, FileSystemLoader

class str_item:
  def __init__(self, n, l):
    self.number = n
    self.log10 = l

if __name__ == "__main__":
  input_precision = 2 
  output_precision = 3
  mp.dps = output_precision + 10
  
  table_raw = []
  number = mp.mpf(1.0)
  while number <= mp.mpf(10.0):
    table_raw.append([number, mp.log10(number)])
    number = number + mp.power(10, -input_precision)
  
  table = []
  with mp.workdps(output_precision):
    table = [str_item(row[0], row[1]) for row in table_raw]
  
  latex_renderer = Environment(
    block_start_string = "%{",
    block_end_string = "%}",
    variable_start_string = "%{{",
    variable_end_string = "%}}",
    loader = FileSystemLoader("."))
  template = latex_renderer.get_template("template.tex")
  
  with open("log_table.tex", mode="w") as f:
    f.write(template.render(table=table))
