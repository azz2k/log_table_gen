from mpmath import mp
from jinja2 import Environment, FileSystemLoader

class str_item:
  def __init__(self, n, l):
    self.number = n
    self.log10 = l

if __name__ == "__main__":
  input_dps = 5
  output_dps = 72
  rows_per_page = 50
  mp.dps = output_dps + 10
  
  table_raw = []
  for number in mp.arange(1.0, 10.0, mp.power(10, -(input_dps-1))):
    table_raw.append([number, mp.log10(number)])
  
  table_str = []
  table_str = [str_item(mp.nstr(row[0], input_dps), mp.nstr(row[1], output_dps)) for row in table_raw]

  pages = [table_str[i:i+rows_per_page] for i in range(0, len(table_str), rows_per_page)]
  
  latex_renderer = Environment(
    block_start_string = "%{",
    block_end_string = "%}",
    line_statement_prefix = "%#",
    variable_start_string = "%{{",
    variable_end_string = "%}}",
    loader = FileSystemLoader("."))
  template = latex_renderer.get_template("template.tex")
  
  with open("log_table.tex", mode="w") as f:
    f.write(template.render(pages=pages))
