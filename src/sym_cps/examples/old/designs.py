# type: ignore
import json

from sym_cps.representation.tools.parsers.parse import parse_library_and_seed_designs

# from simple_uam import direct2cad
from sym_cps.tools.io import save_to_file

c_library, designs = parse_library_and_seed_designs()
c_trowel, t_trowel = designs["Trowel"]

# t_trowel.graph.vs["label"] = t_trowel.graph.vs[""]

# p = igraph.plot(t_trowel.graph,
#                 vertex_label = labels,
#                 vertex_size = 32,
#                 vertex_frame_width = 0.0,
#                 vertex_color = '#AAAAFF')

print(t_trowel.graph.write_dot("trowel.dot"))

params = {
    "Param_0": 1650,
    "Param_1": 2000,
    "Param_10": 45,
    "Param_11": 10000,
    "Param_12": 1000,
    "Param_14": 4500,
    "Param_15": 25,
    "Param_16": 790,
    "Param_17": 210,
    "Param_18": -210,
    "Param_19": 315,
    "Param_2": 12,
    "Param_3": 1000,
    "Param_4": 150,
    "Param_5": 2000,
    "Param_6": 1520,
    "Param_7": 200,
    "Param_8": 300,
    "Param_9": 150,
}


save_to_file(json.dumps(c_trowel.to_design_swri), "trowel_original_design_swri.json")

for param, value in params.items():
    c_trowel.design_parameters[param].value = value


save_to_file(json.dumps(c_trowel.to_design_swri), "trowel_original_modified_swri.json")
