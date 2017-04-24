# -*- coding: utf-8 -*-
from __future__ import division
from app.calc import rub_comma, okrug2

# Типографские расходы
white_paper_batch_cost_65 = 80
white_sheets_per_batch_65 = 250

color_paper_batch_cost = 650
color_sheets_per_batch = 250

pages_count = 100

while pages_count % 4:
    pages_count += 1

layout_sheets = pages_count // 4

print rub_comma(45.37)
print pages_count
print layout_sheets
