# type: ignore
import json

from sym_cps.optimizers.concrete_opt import ConcreteOptimizer, ConcreteStrategy
from sym_cps.optimizers.params_opt import ParametersOptimizer
from sym_cps.optimizers.topo_opt import TopologyOptimizer, TopologyStrategy
from sym_cps.representation.design.concrete import DConcrete
from sym_cps.representation.design.topology import DTopology
from sym_cps.representation.tools.parsers.parse import parse_library_and_seed_designs
from sym_cps.shared.paths import output_folder
from sym_cps.representation.tools.parsers.parsing_designs import parse_design_from_design_swri


c_library, designs = parse_library_and_seed_designs()

topo_opt = TopologyOptimizer(library=c_library)
concr_opt = ConcreteOptimizer(library=c_library)
para_opt = ParametersOptimizer(library=c_library)

if __name__ == "__main__":
    """Read from design_swri"""
    design_swri_path = output_folder / "seed_designs" / "Rake_design_swri.json"
    design = parse_design_from_design_swri(path=design_swri_path, library=c_library)
    print(design)
    """Generate Topology DTopology"""
    d_topology: DTopology = topo_opt.generate_topology(
        strategy=TopologyStrategy.random_strategy
    )

    # print(d_topology)

    """Refine DTopology to DConcrete"""
    d_concrete: DConcrete = concr_opt.concretize_topology(
        d_topology=d_topology, strategy=ConcreteStrategy.random_strategy
    )
    # print(d_concrete)

    test = d_concrete.to_design_swri
    output_path = (
        output_folder / "custom_designs" / f"{d_concrete.name}_design_swri.json"
    )
    with open(output_path, "w") as output_file:
        json.dump(d_concrete.to_design_swri, output_file, indent=4)

    # msg = direct2cad.process_design.send(d_concrete.to_design_swri)

    """Optimize Parameters of DConcrete"""
    # TODO
