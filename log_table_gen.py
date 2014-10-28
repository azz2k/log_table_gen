from mpmath import mp
from jinja2 import Environment, FileSystemLoader

class str_item:
  def __init__(self, n, l):
    self.number = n
    self.log10 = l

if __name__ == "__main__":
  input_dps = 3
  output_dps = 6
  mp.dps = output_dps + 10
  
  table_raw = []
  for number in mp.arange(1.0, 10.0, mp.power(10, -(input_dps-1))):
    table_raw.append([number, mp.log10(number)])
  
  table = []
  table = [str_item(mp.nstr(row[0], input_dps), mp.nstr(row[1], output_dps)) for row in table_raw]
  
  latex_renderer = Environment(
    block_start_string = "%{",
    block_end_string = "%}",
    variable_start_string = "%{{",
    variable_end_string = "%}}",
    loader = FileSystemLoader("."))
  template = latex_renderer.get_template("template.tex")
  
  with open("log_table.tex", mode="w") as f:
    f.write(template.render(table=table))
