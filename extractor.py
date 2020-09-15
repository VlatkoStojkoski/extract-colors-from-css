import json
import re
import requests
import datetime

with open("source.css", "r") as sf:
  css_lines = sf.readlines()

colors = []

for index, line in enumerate(css_lines, start=1):
  if re.search(".*{.*", line):
    selector =  re.findall(".*{.*", line)[0]

  elif re.search(".*((#[A-Wa-w0-9])|((rgb|rgba)\(.*\))).*;$", line):
    detected_line = re.search(".*((#[A-Wa-w0-9])|((rgb|rgba)\(.*\))).*;$", line).group(0)
    
    color = re.findall('(#[A-Wa-w0-9]*)|((rgb|rgba)\(.*\))', detected_line)[0][0].lstrip("#")
    color_name = requests.get(f"https://api.color.pizza/v1/{color[0:6]}").json()["colors"][0]["name"]

    colors.append({
      "selector": selector.strip().strip('{').strip(),
      "property": detected_line.strip().strip(';').strip(),
      "color": f"#{color}",
      "color-name": re.sub("\s", "-", color_name).lower(),
      "line": index
    })
    
with open('colors.pallete', 'w') as outfile:
  json.dump(colors, outfile)