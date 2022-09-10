import os

param = {
    'imp-states': 2800, 
    'imp-segment': 7, 
    'imp-step': 0.05260787840146851, 
    'imp-nsteps': 7, 'ne': 480000, 
    'overlap': 4, 
    'window': 65
}

params = f"imp-states={param['imp-states']} imp-segment={param['imp-segment']} imp-step={param['imp-step']} imp-nsteps={param['imp-nsteps']} ne={param['ne']} overlap={param['overlap']} window={param['window']}"

def impute(crop, region, input_bytes: bytes) -> bytes:
    target_name = 'target.vcf.gz'
    with open(target_name, 'wb') as target_file:
        target_file.write(input_bytes)

    ref_name =  './ref/cucumber_impute_Chr1.vcf.gz'
    prefix = 'out.ref'

    trash = os.system(f"""
        java -jar beagle.22Jul22.46e.jar gt={target_name}
        ref={ref_name} out={prefix} {params}""")
    print(trash)
    
    out_name = f"{prefix}.vcf.gz"
    with open(out_name, "rb") as out_file:
        output_bytes = out_file.read()

    print(len(input_bytes), len(output_bytes))

    return out_name