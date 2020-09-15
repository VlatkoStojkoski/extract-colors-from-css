import json
import re

with open("colors.pallete") as json_file:
  pallete = json.load(json_file)

with open("source.css") as css_file:
  css = css_file.readlines()

root_vars = ""

for color in pallete:
  root_vars += f"  --{color['color-name']}: {color['color']};\n"
  css[color["line"]-1] = re.sub(color["color"], f"var(--{color['color-name']})", css[color["line"]-1])

with open("replaced.css", "w") as outfile:
  outfile.write(":root {\n" + root_vars + "}\n\n" + "".join(css))